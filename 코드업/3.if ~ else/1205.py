a,b = map(float,input().split())

do = a+b,b+a,a-b,b-a,a*b,b*a,a/b,b/a,a**b,b**a

print(f"{max(do):.6f}")