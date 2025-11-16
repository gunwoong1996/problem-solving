
a,m,d,n = map(int,input().split()) #시작 값,곱할 값,더할 값,몇번 째 수

for i in range(n-1):
    a = (a*m)+d


print(a)
