n, k = map(int, input().split())
a = list(map(int, input().split()))

weights = [1 + x for x in a] 
weights.sort()

total = 0
count = 0
for w in weights:
    if total + w <= k:
        total += w
        count += 1
    else:
        break

print(count)