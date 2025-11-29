num1,cal,num2 = input().split()

num1 = int(num1)

num2 = int(num2)


if cal == '+':
    print(num1+num2)

elif cal == '-':
    print(num1-num2)

elif cal == '*':
    print(num1*num2)

elif cal == '/':
    print(f"{num1/num2:.2f}")

