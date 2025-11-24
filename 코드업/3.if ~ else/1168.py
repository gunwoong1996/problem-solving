birth, gender = input().split()

year = int(birth[:2])  # 연도 두 자리

# 성별로 세기 결정
if gender in ['1', '2']:
    year += 1900
else:  # 3 또는 4
    year += 2000

age = (2012 - year) + 1   # 한국식 나이

print(age)