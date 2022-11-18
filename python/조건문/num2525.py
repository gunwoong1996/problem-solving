#오븐 시계

Hour, Minute = map(int, input().split())
timer = int(input())

Hour += int(timer / 60)
Minute += int(timer % 60)

if Minute >= 60:
    Hour += 1
    Minute -= 60
if Hour >= 24:
    Hour -= 24
    
print(Hour,Minute)