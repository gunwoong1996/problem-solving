word = input().lower()  # 🔹 대소문자 통일

sum1 = 0
sum2 = 0

# "C" 개수
for i in word:
    if i == 'c':
        sum1 += 1

# "CC" 개수 (연속, 겹침 허용)
for j in range(len(word) - 1):
    if word[j] == 'c' and word[j + 1] == 'c':
        sum2 += 1

print(sum1)
print(sum2)