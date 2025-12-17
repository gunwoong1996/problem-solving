n = int(input())  

# 위쪽
for i in range(1, 2*n, 2):
    if i % 2 == 1:
        print(" " * ((2*n - 1 - i)//2) + "*" * i)

# 아래쪽
for i in range(2*n - 3, 0, -2):
    if i % 2 == 1:
        print(" " * ((2*n - 1 - i)//2) + "*" * i)