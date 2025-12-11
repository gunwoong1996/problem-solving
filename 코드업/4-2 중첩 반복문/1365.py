n = int(input())

for r in range(n):
    for c in range(n):
        if r == 0 or r == n-1 or c == 0 or c == n-1 or r == c or r + c == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()