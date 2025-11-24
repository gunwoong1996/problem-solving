age = int(input())

year = 2012 - age + 1  # 출생년도 계산

if year < 2000:
    print(f"{year % 100} 1")
else:
    print(f"{year % 100} 3")