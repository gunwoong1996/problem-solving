n = int(input())

cnt = 0

for i in range(0,n):
    if i % 10 == 1 or i == 1 :
        cnt += 1

print(cnt)