s = input()

result = ""
result2 =""

for i in s:
    result += chr(ord(i) + 2)
    result2 += chr((ord(i) *7) % 80 + 48 )


print(result)
print(result2)