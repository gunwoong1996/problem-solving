#별 찍기 - 2
star = int(input())

for i in range(star):
    i += 1
    print(" " * (star-i) + "*" *i)