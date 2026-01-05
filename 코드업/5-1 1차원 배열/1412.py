s = input().lower()   # 소문자로 변환

cnt = [0] * 26        # a~z 개수 저장

for ch in s:
    if 'a' <= ch <= 'z':
        cnt[ord(ch) - ord('a')] += 1

print(*cnt)