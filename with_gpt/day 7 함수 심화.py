#day 7 함수 심화

# 미션1
# power(base, exp=2) 함수를 만들어서, 기본값으로 제곱을 계산하게 해보기

def power(base,exp=2):
    return base ** exp

num = int(input("숫자 입력:"))
print("제곱:", power(num))       # 기본값 exp=2 → 제곱3
print("세제곱:", power(num, 3))  # exp=3 → 세제곱

# 미션2
# sum_all(*args) 함수를 만들어서, 전달된 모든 숫자의 합을 구하기

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1,2,3))
