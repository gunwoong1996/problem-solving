n = int(input()) #n<=1000

nums = list(map(int,input().split()))


nums.sort()
print(nums[n-1])


