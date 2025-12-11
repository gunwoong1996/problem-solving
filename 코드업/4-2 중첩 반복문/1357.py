n = int(input())  # 삼각형의 길이

cnt = n

for i in range(1,n+1):
    
    print("*"*i)

for j in range(1,n+1):
    cnt -=1
    print("*"*cnt)
