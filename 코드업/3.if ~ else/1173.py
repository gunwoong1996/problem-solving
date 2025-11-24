a,b, = map(int,input().split())

time = b-30

if time<0:
    a-1
    print(a,time)

else:
    print(a,time)