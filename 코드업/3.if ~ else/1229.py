height,weight = map(float,input().split())

average = 0
if height<150:
    average = height -100

elif 150<=height<160:
    average = (height -150)/2 + 50

elif height>=160:
    average = (height-100)*0.9

heavy = (weight - average) * 100 / average # 비만도 10 이하 정상 , 10초과 20이하 과체중 , 20초과 비만

if heavy <= 10:
    print("정상")

elif 20>=heavy>10:
    print("과체중")

elif heavy>20:
    print("비만")
