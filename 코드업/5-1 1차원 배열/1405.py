k = int(input())  

num = list(map(int,input().split()))

for i in range(k):
    print(*(num[i:] + num[:i]))