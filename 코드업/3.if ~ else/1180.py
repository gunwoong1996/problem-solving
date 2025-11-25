n = int(input())

ten = n // 10 #10의 자리
one = n % 10 #1의 자리

change = one * 10 + ten
result = change * 2


if result>99:
    print(result-100)

else:
    print(result) 

if (result-100) <= 50:
    print("GOOD")
elif (result-100)>=50:
    print("OH MY GOD")

