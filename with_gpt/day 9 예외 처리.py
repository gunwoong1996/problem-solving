#day 9 예외 처리

#  try:
#      실행할 코드
#  except:
#      에러 발생 시 실행할 코드 


# 미션1
"""숫자 두 개를 입력받아 나누기 결과 출력하기

만약 0으로 나누면 "0으로 나눌 수 없습니다. 출력

숫자가 아닌 걸 입력하면 "숫자를 입력해야 합니다. 출력"""

# 미션2

try:
   num1 = int(input("숫자1 입력:"))
   num2 = int(input("숫자2 입력:"))

   result = num1/num2

   print("나눈 결과값은?",result)

except ZeroDivisionError:
   print("0으로 나눌 수 없습니다")

except ValueError:
   print("숫자를 입력해야합니다")
   

