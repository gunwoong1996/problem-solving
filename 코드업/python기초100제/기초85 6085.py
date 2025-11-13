
r,g,b = map(int,input().split())

mb = r*g*b/8/1024/1024

print(f"{mb:.2f} MB")