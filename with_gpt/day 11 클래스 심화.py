#day 11 클래스와 심화



# 미션1
"""
1.Vehicle 클래스를 만들고, drive() 메서드에서 "차량이 움직입니다." 출력

2.Car 클래스가 Vehicle을 상속받아, drive() 메서드를 "자동차가 달립니다." 로 오버라이딩
"""
class Vehicle: #부모 클래스
    def __init__(self,name):
        self.name = name

    def drive(self): #매서드
        print("차량이 움직입니다")

class Car(Vehicle): #자식 클래스
    def drive(self): #매서드
        super().drive()
        print("자동차가 달립니다")

c1 = Car("포르쉐")
c1.drive()

# 미션2



# 부모 클래스의 메서드를 자식 클래스에서 덮어쓰기 가능

class Animal: #부모 클래스
    def __init__(self,name):
        self.name = name

    def sound(self):
        print("동물이 내는 소리")

class Dog(Animal): #자식 클래스
    def sound(self):
        print("멍멍")


class Cat(Animal): #자식 클래스2
    def sound(self):
        print("야옹")

class Bird(Animal):
    def sound(self):
        super().sound() #부모 클래스 호출
        print("짹쨱")

dog = Dog("깜순")
cat = Cat("나비")
bird = Bird("앵무")

dog.sound()
cat.sound()
bird.sound()