expr = input().strip()

num = 0            # 현재 읽는 숫자
result = None      # 계산 결과
op = None          # 직전 연산자

for ch in expr:
    if ch.isdigit():          # 숫자라면 이어 붙이기
        num = num * 10 + int(ch)
    else:                     # 연산자 (+ - * / =) 를 만났을 때
        if result is None:
            result = num     # 첫 숫자일 때
        else:
            if op == '+':
                result += num
            elif op == '-':
                result -= num
            elif op == '*':
                result *= num
            elif op == '/':
                result //= num   # 정수 나눗셈

        if ch == '=':         # '='이면 끝
            break

        op = ch               # 새로운 연산자 저장
        num = 0               # 숫자 초기화

print(result)