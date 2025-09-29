#day 10 클래스와 객체



# 미션1
"""Dog 클래스를 만들고, 이름과 나이를 저장한 뒤
"멍멍! 저는 OOO, 나이는 XX살입니다." 출력하는 메서드 작성하기"""

# 미션2

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def dogprofile(self):
        print(f"멍멍! 저는 {self.name} , 나이는 {self.age}살입니다.")


d1 = Dog("깜순",3)
d1.dogprofile()


