#주사위 세개

A,B,C=map(int,input().split())

if(A==B==C): #1
    print(10000+(A*1000))

elif(A==B or A==C or B==C): #2
    if(A==B): 
        print(1000+(A*100))
    if(A==C): 
        print(1000+(A*100))
    if(B==C): 
        print(1000+(B*100))

else: #3
    print(max(A,B,C)*100)
    
