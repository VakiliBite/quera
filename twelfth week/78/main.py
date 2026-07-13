n, k = map(int, input().split())
a = list(map(int, input().split()))

photos = 1
current = 0

for x in a:
    if current + x <= k:
        current += x
    else:
        photos += 1
        current = x

print(photos)