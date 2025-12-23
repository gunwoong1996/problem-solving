word = input().lower()  #  대소문자 통일


cnt = 0

for i in word:
    cnt+=1
    if i == "t":
        print(cnt,end=" ")
        