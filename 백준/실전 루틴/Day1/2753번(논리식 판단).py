year = int(input("년도를 입력하시오:"))


if year == (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print("1")
else:
    print("0")



#백준 버젼

if (((year%4) == 0) and ((year%100 != 0) or ((year%400) == 0))):
    print("1")
else:
    print("0")