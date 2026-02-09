import os
import json
from datetime import datetime

import streamlit as st
from openai import OpenAI

# =========================
# 1) 기본 설정
# =========================
APP_TITLE = "🤖 Smart Assistant"
MODEL = "gpt-4.1-mini"

# (대략) gpt-4.1-mini 단가(USD) — 나중에 바뀌면 여기만 수정
# input: $0.40 / 1M tokens, output: $1.60 / 1M tokens
PRICE_PER_1M_INPUT = 0.40
PRICE_PER_1M_OUTPUT = 1.60

# 월 예산 (USD) — 예: $5면 보통 공부용으로 꽤 씀
MONTHLY_BUDGET_USD = 5.0

USAGE_FILE = "usage.json"

SYSTEM_PROMPT = """너는 파이썬 코딩 튜터이자 업무 비서다.
사용자가 코드/질문을 주면 아래 형식으로 한국어로 답한다.

[1] 한줄 결론
[2] 정답/수정 코드(필요할 때만)
[3] 설명(초보 친화)
[4] 주의점/팁
[5] 다음 행동/미니 연습문제 1개

추가 규칙:
- 코드가 들어오면 버그/개선점/정답을 우선 제시.
- 질문이 업무(정리/메모/문장다듬기/회의안건/계획)면 비서처럼 도와준다.
- 불확실하면 추측하지 말고 가정/전제조건을 명시한다.
"""


# =========================
# 2) 월별 사용량 저장/예산 제한
# =========================
def month_key(dt: datetime) -> str:
    return dt.strftime("%Y-%m")


def load_usage() -> dict:
    if not os.path.exists(USAGE_FILE):
        return {}
    try:
        with open(USAGE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_usage(data: dict) -> None:
    with open(USAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def estimate_cost_usd(input_tokens: int, output_tokens: int) -> float:
    return (input_tokens / 1_000_000) * PRICE_PER_1M_INPUT + (output_tokens / 1_000_000) * PRICE_PER_1M_OUTPUT


def get_month(data: dict, mk: str) -> dict:
    if mk not in data:
        data[mk] = {"usd": 0.0, "input_tokens": 0, "output_tokens": 0, "calls": 0}
    return data[mk]


def add_spend(data: dict, mk: str, usd: float, in_tok: int, out_tok: int) -> None:
    m = get_month(data, mk)
    m["usd"] = float(m["usd"]) + float(usd)
    m["input_tokens"] = int(m["input_tokens"]) + int(in_tok)
    m["output_tokens"] = int(m["output_tokens"]) + int(out_tok)
    m["calls"] = int(m["calls"]) + 1


# =========================
# 3) Streamlit UI
# =========================
st.set_page_config(page_title="Smart Assistant", page_icon="🤖", layout="centered")
st.title(APP_TITLE)
st.caption("파이썬 질문/코드 + 비서 업무(정리/작성/계획)까지. 월 예산 제한 포함.")

# 세션 대화 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕! 파이썬 질문이나 코드, 또는 업무 요청(정리/문장/회의안건) 뭐든 던져줘."}
    ]

usage = load_usage()
mk = month_key(datetime.now())
m = get_month(usage, mk)

# 사이드바: 예산/사용량/설정
with st.sidebar:
    st.subheader("설정 / 예산")
    st.write(f"- 모델: **{MODEL}**")
    st.write(f"- 이번 달 호출 수: **{m['calls']}**")
    st.write(f"- 이번 달 사용액(USD): **${m['usd']:.4f}**")
    st.write(f"- 월 예산(USD): **${MONTHLY_BUDGET_USD:.2f}**")
    st.write(f"- Input tokens: **{m['input_tokens']}**")
    st.write(f"- Output tokens: **{m['output_tokens']}**")

    if st.button("대화 초기화"):
        st.session_state.messages = [
            {"role": "assistant", "content": "대화를 초기화했어. 다시 시작해보자!"}
        ]
        st.rerun()

    if st.button("이번 달 사용량 초기화(usage.json)"):
        usage[mk] = {"usd": 0.0, "input_tokens": 0, "output_tokens": 0, "calls": 0}
        save_usage(usage)
        st.rerun()

    st.divider()
    st.write("팁: 비용 아끼려면 질문을 짧고 구체적으로!")
    st.subheader("API Key")

    api_key_input = st.text_input(
    "OpenAI API Key (sk-로 시작)",
    type="password",
    value=st.session_state.get("api_key", ""),
    help="환경변수 꼬일 때 대비용. 여기에 넣으면 바로 적용됨."
    )
    if api_key_input:
        st.session_state["api_key"] = api_key_input.strip()

    st.caption("※ 키는 저장소(Git)에 올리지 마세요.")

    

# 대화 렌더링
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


def call_ai(user_text: str) -> str:
    # 0) 키 확보: (1) 사이드바 입력 > (2) 환경변수
    api_key = (st.session_state.get("api_key") or os.getenv("OPENAI_API_KEY") or "").strip()

    if not api_key:
        return (
            "API 키가 없어.\n\n"
            "해결:\n"
            "1) 왼쪽 사이드바에 API 키를 넣거나\n"
            "2) cmd에서 setx OPENAI_API_KEY \"sk-...\" 설정 후 재실행\n"
        )

    # ✅ 호출할 때마다 클라이언트 생성(키 전달 100% 보장)
    client = OpenAI(api_key=api_key)

    # (이 아래는 네 기존 예산 체크/호출 로직 그대로)
    current_spent = float(get_month(usage, mk)["usd"])
    if current_spent >= MONTHLY_BUDGET_USD:
        return (
            "이번 달 예산을 초과했어. 호출을 막았어.\n\n"
            f"- 이번 달 사용액: ${current_spent:.4f}\n"
            f"- 월 예산: ${MONTHLY_BUDGET_USD:.2f}\n"
        )

    resp = client.responses.create(
        model=MODEL,
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text},
        ],
    )

    text = resp.output_text or "(출력이 비어있어. 질문을 조금 더 구체적으로 해줘.)"

    in_tok = 0
    out_tok = 0
    try:
        u = getattr(resp, "usage", None)
        if u:
            in_tok = int(getattr(u, "input_tokens", 0) or 0)
            out_tok = int(getattr(u, "output_tokens", 0) or 0)
    except Exception:
        pass

    cost = estimate_cost_usd(in_tok, out_tok)
    add_spend(usage, mk, cost, in_tok, out_tok)
    save_usage(usage)

    new_total = float(get_month(usage, mk)["usd"])
    return text + f"\n\n---\n(이번 호출 추정: ${cost:.6f} / 이번 달 누적: ${new_total:.4f})"

# 입력 받기
user_input = st.chat_input("질문/코드/업무요청을 입력하세요…")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    reply = call_ai(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
