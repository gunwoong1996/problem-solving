menu = {
    1: 400,   # 치즈버거
    2: 340,   # 야채버거
    3: 170,   # 우유
    4: 100,   # 계란말이
    5: 70     # 샐러드
}

a, b = map(int, input().split()) 

total = menu[a] + menu[b]

if total > 500:
    print("angry")
else:
    print("no angry")