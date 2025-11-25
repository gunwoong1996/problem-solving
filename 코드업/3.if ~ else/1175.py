day = int(input())

weekday = (day - 1) % 7  # 1일이 월요일이므로 0부터 시작

if weekday <= 4:
    print("주중")
else:
    print("주말")


print(5%7)