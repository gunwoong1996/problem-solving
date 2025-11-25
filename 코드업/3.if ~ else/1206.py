a,b = map(int,input().split())


if b % a == 0 :
    
    print(f"{a}*{b/a:.0f}={b}") 

elif a % b == 0:
    
    print(f"{b}*{a/b:.0f}={a}")

elif a == b :
    print(f"{a}*1={b}")


elif a % b !=0 and b % a != 0:
    print("none")