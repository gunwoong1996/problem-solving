a,b,c = list(map(int,input().split())) #터널 3개의 높이

carheight = 170

tunnel = [a,b,c]

#tunnel.sort() #터널 높이 오름차순


for i in tunnel:
    if i <=170:
        print("CRASH",i)
        break
else:
    print("PASS")



