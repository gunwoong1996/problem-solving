# 6자리 숫자로 이루어진 연월일(YYMMDD)이 입력된다.

# 년도(YY) 월(MM) 일(DD)을 공백으로 구분해 한 줄로 출력한다.


s = input()

print(s[0:2],s[2:4],s[4:6])

print(s[2:4],end="")

print(s[4:6])
