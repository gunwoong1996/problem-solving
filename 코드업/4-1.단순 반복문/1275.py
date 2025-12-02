n, k = map(int, input().split())

result = 1
for _ in range(k):
    result *= n

print(result)

# n, k = map(int, input().split())

# result = 1
# count = 0

# while count < k:
#     result *= n
#     count += 1

# print(result)