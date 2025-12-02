n = int(input()) #데이터의 개수 (홀수)

nums = list(map(int,input().split()))

center = int(n/2 - (0.5))

if n % 2 == 0:
    print(f"{nums[0],nums[n/2],nums[n-1]}")

elif n % 2 == 1:
    print(nums[0],nums[center],nums[n-1])


