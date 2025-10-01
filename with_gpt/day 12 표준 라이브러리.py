#day 12 표준 라이브러리

import random #난수 무작위값

print(random.randint(1,6)) # 1~6 사이 무작위 정수 (주사위)
print(random.choice(["치킨","피자","햄버거"]))

import datetime # 현재 날짜 시간 다루기

now = datetime.datetime.now()
print("현재 시각: ",now)
print("오늘 날짜: ",now.date())
print("현재 시간: ",now.time())

import math #기본 연산보다 복잡한 수학 기능 제공

print(math.sqrt(16)) #제곱
print(math.factorial(5)) # 5! 
print(math.pi) #원주율

# 미션1

#random.randint() 를 사용해 주사위를 굴려서 1~6 중 하나 출력하기

print(random.randint(1,6))

# 미션2

#오늘 날짜와 요일을 출력하기

print("오늘 날짜: ",now.date())
print("오늘 요일: ",now.strftime('%A'))

# 미션3

#math.sqrt() 로 입력받은 숫자의 제곱근을 출력하기

print(math.sqrt(4))