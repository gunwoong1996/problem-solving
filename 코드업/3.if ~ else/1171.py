a,b,c = map(int,input().split())

if b<10 and 10<c<100:
    print(f"{a}0{b}0{c}")

elif b<10 and c<10:
    print(f"{a}0{b}00{c}")
elif b<10 and c>100:
    print(f"{a}0{b}{c}")
elif b>10 and c<10:
    print(f"{a}{b}00{c}")
elif b>10 and 100>c>10:
    print(f"{a}{b}0{c}")

else:
     print(f"{a}{b}{c}")


# a, b, c = map(int, input().split())

# print(f"{a}{b:02d}{c:03d}")