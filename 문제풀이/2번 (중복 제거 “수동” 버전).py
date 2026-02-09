def unique_keep_order(nums):
    result = []
    for n in nums:
        if n not in result:
            result.append(n)
    return result

nums = [4, 2, 2, 1, 3, 4]
print(unique_keep_order(nums))