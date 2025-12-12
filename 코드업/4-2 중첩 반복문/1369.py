n, k = map(int, input().split())

for i in range(n):
    for j in range(n):
        # 테두리
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="")
        # 반대 방향 빗금
        elif (i + j) % k == k - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()