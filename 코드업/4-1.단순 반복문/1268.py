n = int(input())

nums = list(map(int,input().split()))


sum = 0

for i in range(0,n):
    if nums[i] % 2 == 1:
        sum += 1

print(sum)