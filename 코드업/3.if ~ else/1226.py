# 당첨 번호 + 보너스 번호 입력
a, b, c, d, e, f, bonus = map(int, input().split())

# 지혜 로또 번호 입력
x, y, z, u, v, w = map(int, input().split())

# 당첨 번호 리스트
win = [a, b, c, d, e, f]

# 지혜 번호 리스트
jihye = [x, y, z, u, v, w]

# 맞은 개수 세기
cnt = 0
for num in jihye:
    if num in win:
        cnt += 1

# 등수 판정
if cnt == 6:
    print("1")
elif cnt == 5 and bonus in jihye:
    print("2")
elif cnt == 5:
    print("3")
elif cnt == 4:
    print("4")
elif cnt == 3:
    print("5")
else:
    print("0")