# 문제 1: 학생 점수 계산기

# 설명:

# 학생 이름과 점수를 받아서 평균을 구하고,
# 클래스 안에서 출력하는 프로그램 만들기.

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)

def print_result(student):
    print(f"{student.name}의 평균 점수는 {student.average():.2f}점입니다.") #.2f 소수점 아래를 2자리까지만 표시하라
 
# 실행 예시
s1 = Student("건웅", [80, 90, 75])
print_result(s1)

""" 문제 2: 은행 계좌 관리 (잔액 계산 함수 분리)

 설명:

 클래스 내부는 계좌 관리,

 외부 함수로는 수수료 계산 기능 추가.

"""

class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self , amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("잔액 부족")


def calc_fee(amount):
    return amount * 0.05


a1 = Account("건웅",10000)
fee = calc_fee(2000)
a1.withdraw(2000+fee)

print(a1.balance)
