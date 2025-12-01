a,b,c,n = map(int,input().split()) #a 시작 값 , b 곱할 값 , c 더할 값 , 몇번째 항 n

sum = a

for i in range(1,n):
    sum = (sum * b) + c

print(sum)