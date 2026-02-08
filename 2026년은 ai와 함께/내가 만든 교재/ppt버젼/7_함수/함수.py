def add(a, b):
    return a + b

print(add(1,2))


def is_even(n):
    return n % 2 == 0

print(is_even(3))



def list_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

result = list_sum([1, 2, 3, 4])
print(result)


def strlen(s):
    return len(s)

print(strlen("sdqd"))


def greet(name='손님'):
    print(name)

print(greet("민수"))

def calc(a, b):
    return a+b, a-b

print(calc(2,3))


def grade(score):
    if score >= 60:
        return '합격'
    return '불합격'

print(grade(59))


def read_int():
    return int(input())

x = read_int()
print(x + 10)


