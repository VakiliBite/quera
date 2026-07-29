n = int(input())

count = 0
total = 0

for d in range(1, n + 1):
    k = n // d
    count += k
    total += d * k

print(count, total)