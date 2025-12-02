n = int(input())

k = 0

t = 0

while n>0:
    n -= 1
    k += 1

    if n / k == 1:
        t = n / k
        print(k,t) 
        break