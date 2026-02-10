def count_numbers(nums):
    counts = {}
    for n in nums:
        if n not in counts:
            counts[n] = 1
        else:
            counts[n] += 1

    return counts


nums = [1, 2, 2, 3, 3, 3]

print(count_numbers(nums))