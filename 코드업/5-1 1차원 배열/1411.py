n = int(input())

cards_sum = 0
for _ in range(n - 1):
    cards_sum += int(input())

total = n * (n + 1) // 2
print(total - cards_sum)