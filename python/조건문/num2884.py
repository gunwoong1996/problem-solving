#알람 시계
H,M=map(int,input().split())

if(M<45):
    H-=1
    M = 60 + (M-45)
    if(H<0):
        H+=24
    print(H,M)
    
else:
    print(H,M)

