fruits = ["사과", "바나나", "포도"]

for i, fruit in enumerate(fruits): #enumerate = 번호 표기
    print(i, fruit)


#==============================================

names = ["철수", "영희", "민수"]
scores = [90, 85, 100]

for name, score in zip(names, scores): # 여러 개의 리스트를 같은 인덱스끼리 묶어서 반복할 때 씀
    print(name, score)

#===================================================

names = ["철수", "영희", "민수"]
scores = [90, 85, 100]

for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{i}번 {name}: {score}점")

#==============================================

arr = [10, 20, 30]
for i in range(len(arr)):
    print(i, arr[i])

for i, v in enumerate(arr, start=1):
    print(i, v)

s = 'python'
for i, ch in enumerate(s):
    print(i, ch)

