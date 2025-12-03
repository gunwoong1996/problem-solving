v = int(input())

result = input().strip()     # 공백 없이도 처리 가능
ac = 0
bc = 0

for ch in result:
    if ch == 'A':
        ac += 1
    elif ch == 'B':
        bc += 1

if ac > bc:
    print("A")
elif ac < bc:
    print("B")
else:
    print("Tie")