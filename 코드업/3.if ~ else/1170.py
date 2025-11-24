a,b,c = map(int,input().split())

if c<10:
    print(f"{a}{b}0{c}")

else:
    print(f"{a}{b}{c}")