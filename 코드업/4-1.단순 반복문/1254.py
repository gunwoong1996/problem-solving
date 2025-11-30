a, b = input().split()

start = ord(a)   # 문자 → 아스키코드
end = ord(b)

if start <= end:
    for i in range(start, end + 1):
        print(chr(i), end=' ')
else:
    for i in range(end, start + 1):
        print(chr(i), end=' ')