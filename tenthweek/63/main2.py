n, k = map(int, input().split())

fruits = []

for _ in range(n):
    b, a = map(int, input().split())
    if a > b:
        fruits.append((b, a))

fruits.sort()

for b, a in fruits:
    if k >= b:
        k += a - b

print(k)