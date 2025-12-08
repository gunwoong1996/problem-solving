n = int(input())

for i in range(2, n):
    if n % i == 0:           # i가 약수냐?
        j = n // i           # 짝 약수

        # i가 소수인지 확인 (약수 개수로)
        c1 = 0
        for x in range(1, i+1):
            if i % x == 0:
                c1 += 1

        # j가 소수인지 확인
        c2 = 0
        for y in range(1, j+1):
            if j % y == 0:
                c2 += 1

        if c1 == 2 and c2 == 2:   # 둘 다 소수면
            if i < j:
                print(i, j)
            else:
                print(j, i)
            break
else:
    print("wrong number")