#day 14 클래스심화

#캡슐화

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # __ 두 개로 private 처리

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("잔액이 부족합니다.")

    def get_balance(self):
        return self.__balance


account = BankAccount("건웅",10000)
account.deposit(5000)
account.withdraw(3000)
print(account.get_balance())

#상속

# 부모 클래스의 기능을 자식 클래스가 물려받는 것

# 중복 코드를 줄이고, 재사용성을 높인다.

# 자식 클래스는 필요할 때 부모 메서드를 재정의(오버라이딩) 할 수 있다.

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("동물이 소리를 냅니다!")

# 자식 클래스
class Dog(Animal):
    def sound(self):
        print("멍멍!")

class Cat(Animal):
    def sound(self):
        print("야옹!")

class Bird(Animal):
    def sound(self):
        print("짹짹!")

# 실행
dog1 = Dog("깜순")
cat1 = Cat("나비")
bird1 = Bird("앵무")

dog1.sound()
cat1.sound()
bird1.sound()