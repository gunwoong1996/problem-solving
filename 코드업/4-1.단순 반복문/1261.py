import random

nums = list(map(int, input().split()))


five = [] #5의 배수 저장 리스트

for i in range(nums[0],nums[9]):
    if nums[i] % 5 == 0:
        five.append(nums[i])


if five:
    print(random.choice(five))

else:
    print(0)
