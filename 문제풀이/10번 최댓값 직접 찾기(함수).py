nums = [3, 7, 2, 9, 5]


def find_max(nums):
    max_value = nums[0]

    for n in nums:
        if n> max_value:
            max_value = n
            
    return max_value


print(find_max(nums))