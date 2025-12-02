a,b = map(int,input().split())

result = 0

for i in range(a,b+1):
    if i % 2 == 1:
        result += i
        if i==a:
            print(f"{i}",end ="")
        else:
            print(f"+{i}",end ="")
    
    elif i % 2 == 0:
        result -= i
        print(f"-{i}",end ="")


if result<0:
     print("=",result,sep='')
else:
    print("=",result,sep='')
