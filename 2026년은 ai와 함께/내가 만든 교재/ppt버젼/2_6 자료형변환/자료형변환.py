# a, b = input().split()

# print(a + b)      # 문자열 결합
# print(int(a) + int(b))  # 숫자 덧셈


nums = list("12,3")
print(nums)


data = "10,20,30"
nums = list(map(int, data.split(',')))
print(nums)

arr = [1, 2]
if int(len(arr)) >= 2:
    print("길다")

s = ""
n = int(s) if s else 0
print(n)

#입력값은 항상 문자열이므로 형 변환은 선택이 아니라 필수다
