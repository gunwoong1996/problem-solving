cipher = input()

result = ""

for ch in cipher:
    if ch == " ":               # 공백은 그대로
        result += ch
    else:
        # ch 를 a~z 범위로 암호 해독
        result += chr((ord(ch) - ord('a') + 3) % 26 + ord('a'))

print(result)