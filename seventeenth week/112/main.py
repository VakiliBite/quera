n = int(input())
arr = list(map(int, input().split()))

current = 0
best = 0
for x in arr:
    current += x

    if current < 0:
        current = 0

    if current > best:
        best = current

print(best)