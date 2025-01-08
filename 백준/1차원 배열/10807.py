# 백준 10807번 - 개수 세기

# 입력 받기
n = int(input())  # 숫자의 개수
numbers = list(map(int, input().split()))  # 숫자 리스트
v = int(input())  # 찾고자 하는 숫자

# 리스트에서 v의 개수를 세기
count = numbers.count(v)

# 결과 출력
print(count) #