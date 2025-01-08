#시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 
# 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

#0<=점수<=100

num=int(input())

if(90<=num<=100):
    print("A")

elif(80<=num<=89):
    print("B")

elif(70<=num<=79):
    print("C")

elif(60<=num<=69):
    print("D")

else:
    print("F")