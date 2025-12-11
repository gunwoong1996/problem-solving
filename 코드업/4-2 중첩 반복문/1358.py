n = int(input())  # 3<=n<=99 , n은 반드시 홀수 

cnt = n // 2 

for i in range(1,n+1):
    if i % 2 == 1:
        print(" "*cnt + "*"*i + " "*cnt)
        cnt -=1


