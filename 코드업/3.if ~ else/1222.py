a,b,c = map(int,input().split())

time = 90

for i in range (a,90):
    i +=1
    if i % 5 == 0:
        b+=1


if b > c:
    print("win")

elif b == c:
    print("same")

else:
    print("lose")