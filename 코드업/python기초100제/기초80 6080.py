
a = int(input())

i = 0
sum = 0

for i in range(1,1001):
    #i +=1
    sum +=i
    if sum >= a:
        print(i)
        break
    