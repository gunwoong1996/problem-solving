num = input()

cnt1 = 0
cnt2 = 0

for i in num:
    if i == '(':
        cnt1 += 1
    elif i == ')':
        cnt2 += 1

print(cnt1,cnt2)