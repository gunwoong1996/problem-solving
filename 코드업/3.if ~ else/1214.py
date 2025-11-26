year,month = map(int,input().split())

last ={
    1: 31,2: 28,3: 31,4: 30,5: 31,6: 30,
    7: 31,8: 31,9: 30,10: 31,11: 30,12: 31
}

last2 ={
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


if (year % 400 == 0) or (year % 4 ==0 and year % 100 != 0):
    print(last2[month])

else:
    print(last[month])