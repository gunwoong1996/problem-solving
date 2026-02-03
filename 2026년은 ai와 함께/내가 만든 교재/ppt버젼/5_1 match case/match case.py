"""
menu = int(input())
match menu:
    case 1: print("김밥")
    case 2: print("라면")
    case 3: print("떡볶이") 
    case _: print("메뉴 없음")
"""

#====================================


score = int(input())
match score // 10:
    case 10 | 9: print("A")
    case 8: print("B")
    case _: print("C")

#=========================================
cmd =0

if cmd == "start":
    ...
elif cmd == "stop":
    ...
elif cmd == "restart":
    ...


match cmd:
    case "start":
        ...
    case "stop":
        ...
    case "restart":
        ...