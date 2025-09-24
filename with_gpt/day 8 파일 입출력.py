#day 8 파일 입출력

# 미션1
# memo.txt 파일에 "오늘도 파이썬 공부 중!" 이라는 문장 저장하기

# 미션2
# 그 파일을 다시 읽어서 화면에 출력하기

file = open("memo.txt", "w")  # w: 쓰기 모드
file.write("오늘도 파이썬 공부 중!")
file.close()

file = open("memo.txt", "r")
data = file.read()
file.close()
print(data)