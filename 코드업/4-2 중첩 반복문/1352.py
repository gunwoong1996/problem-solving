a,b = map(int,input().split()) #구구단 시작단과 끝단


for i in range(a,b+1):
    for j in range(1,10):
        print(f"{i}*{j}={i*j}")
   

