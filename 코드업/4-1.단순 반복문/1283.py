a = float(input()) #투자한 액수

b = int(input()) #투자 일수

data = list(map(float,input().split())) #일별 변동폭 데이터

result = a

for i in range(0,b):
    
     result += (result*(data[i]*0.01))

print (f"{result - a:.0f}")

if result>a:
     print("good")
elif result<a:
     print("bad")
elif result == a:
     print("same")
