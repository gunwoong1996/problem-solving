#영수증

sum= int(input())
num = int(input())
result = 0
for i in range(num):
  a,b = map(int, input().split())
  result += a*b
if sum == result:
	print("yes")
else:
	print("no")