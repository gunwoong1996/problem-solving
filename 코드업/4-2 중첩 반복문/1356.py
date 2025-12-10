n = int(input())  # 삼각형의 길이

for i in range(1,n+1):
    if i == n or i == 1:
        print("*"*n)
    else: 
        print("*" + " " *(n-2)+"*")
   