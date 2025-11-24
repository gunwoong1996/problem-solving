a,b, = map(int,input().split())

time = b-30 

if time<0:
    a-=1
    #print(a,(time+60))
    if a<0:
        print(a+24,(time+60))
    else:
        print(a,(time+60))

elif time == 0:
    print(a,0)



else:
    print(a,time)