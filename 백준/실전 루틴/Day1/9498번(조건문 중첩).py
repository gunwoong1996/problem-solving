num = int(input("시험점수를 입력하시오:"))

print(num)

if 100>=num>89:
    print("A")

elif 89>=num>79:
    print("B")

elif 79>=num>69:
    print("C")

elif 69>=num>59:
    print("D")

else:
    print("F")