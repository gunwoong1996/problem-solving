#day 6 함수

# 미션1
# introduce(name, age) 함수를 만들어서 "제 이름은 OOO이고, 나이는 XX살입니다." 출력하기

def introduce(name,age):
    print("제 이름은",name,"이고","나이는",age,"살입니다.")

introduce("건웅","29")


# 미션2
# 두 숫자를 입력받아 합을 돌려주는 add_numbers(a, b) 함수 만들기

def add_numbers(a,b):
    return a+b


num1 = int(input("첫번째 숫자를 입력하시오:"))
num2 = int(input("두번째 숫자를 입력하시오:"))

result = add_numbers(num1,num2)

print("합계:",result)