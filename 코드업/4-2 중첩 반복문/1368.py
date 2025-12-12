h,k,d = input().split() # h = 높이 k = 밑변  방향 = d

h = int(h)

k = int(k)

for i in range(h):
   
    if d == "L":
        print(" "*i +"*"*k)
    elif d == "R":
        print(" "*(h-i-1) +"*"*k)
        