#day 13 모듈과 패키지

import mymath # 다른 파일에서 불러오기

print(mymath.add(3,5))
print(mymath.sub(10,4))


from mymath import add # 모듈 전체가 아니라, 특정 함수만 불러오기

print(add(2,3))

import math as m #모듈 이름 바꾸기
print(m.sqrt(16))



# 미션1
"""
mymath.py 라는 모듈을 만들어서 add, sub, mul, div 함수 정의하기

다른 파일에서 from mymath import add, mul 형태로 불러와서 실행하기
"""

print(mymath.add(5,6))
print(mymath.mul(2,3))


# 미션2


# 미션3
 