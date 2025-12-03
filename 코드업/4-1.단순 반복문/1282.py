n = int(input())

k = 0 #제곱근을 만들기위해 빼야하는 수

t = 0 #제곱근

while n>0:
    n -= 1
    k += 1

    if n % (n ** 0.5) == 0:
        t = n ** 0.5
        print(f"{k} {t:0.0f}") 
        break