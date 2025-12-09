n = int(input())  # 삼각형의 길이

cnt = 0

while n > 0:
    print(" " * cnt, end="")
    print("*" * n)

    n -= 1
    cnt += 1
    