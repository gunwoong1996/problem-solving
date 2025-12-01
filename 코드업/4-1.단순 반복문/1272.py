k,h = map(int,input().split())

sum1 = 0
sum2 = 0

if k % 2 == 0:
   sum1 = k * 5
else:
   sum1 = (k + 1) // 2

if h % 2 == 0:
    sum2 = h * 5
else:
    sum2 = (h + 1) // 2

print(sum1 + sum2)