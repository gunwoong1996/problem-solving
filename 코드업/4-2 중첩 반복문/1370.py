r, h = map(int, input().split())  # r = 한 블록의 높이, h = 블록 반복 횟수

for _ in range(h):
    # 올라가는 부분: 0 ~ r-1
    for i in range(r):
        print(" " * i + "*")
    # 내려가는 부분: r-2 ~ 0
    for i in range(r - 2, -1, -1):
        print(" " * i + "*")