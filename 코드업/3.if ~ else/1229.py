height,weight = map(float,input().split())

# 키에 따른 표준몸무게	공식
# 키가 150 미만일 때	(실제 키 - 100)
# 키가 150이상 160미만일 때	(실제 키 - 150) /2 + 50
# 키가 160 이상일 때	(실제 키 - 100) * 0.9

average = 0 # 표준몸무게

if height < 150:
    average = height -100

elif 150<=height<160:
    average = (height -150)/2 + 50

elif height>=160:
    average = (height - 100) * 0.9


bmi = (weight - average) * 100 / average # 비만도

if bmi<=10:
    print("정상")

elif 10<bmi<=20:
    print("과체중")

elif bmi>20:
    print("비만")