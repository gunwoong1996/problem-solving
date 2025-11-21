a,b=map(int,input().split())
sum = a+b

if a % 2 == 0:
    a = "짝수"
elif a % 2 == 1:
    a = "홀수"

if b % 2 == 0 :
    b = "짝수"

elif b % 2 == 1 :
    b = "홀수"

if sum % 2 == 0:
    sum = "짝수"

elif sum % 2 == 1:
    sum = "홀수"


print(f"{a}+{b}={sum}")