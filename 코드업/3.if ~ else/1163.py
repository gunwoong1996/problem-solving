a,b,c = map(int,input().split())

sum  = a + b + c


if ((sum//100)%10) % 2 == 0:
    print("대박")

else:
    print("그럭저럭")



