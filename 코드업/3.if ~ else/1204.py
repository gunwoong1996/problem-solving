num = int(input())



if num % 10 == 1 and num != 11:
    print(f"{num}st")

elif 20>num>10:
    print(f"{num}th") 

elif num % 10 == 2:
    print(f"{num}nd")

elif num % 10 == 3:
    print(f"{num}rd")



else:
    print(f"{num}th")