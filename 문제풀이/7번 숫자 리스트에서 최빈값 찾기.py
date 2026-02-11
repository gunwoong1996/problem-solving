# 정수 리스트가 주어질 때, 가장 많이 나온 숫자를 반환해라


def most_common_number(nums):
    counts = {}
    for n in nums:
        if n not in counts:
            counts[n] = 1
        else:
            counts[n] += 1

        # 카운트
        pass

    return max(counts, key=counts.get)
   
nums = [1, 3, 2, 3, 1, 4, 3]
print(most_common_number(nums))