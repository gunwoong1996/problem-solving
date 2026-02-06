i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)  #continue = pass / break = end

found = False
i = 0
while i < 5 and not found:
    if i == 4:
        found = True
    i += 1

while True:
    print('1. 시작 2. 종료')
    sel = input()
    if sel == '2':
        break

#종료 조건 설계 중요