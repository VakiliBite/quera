n, m = map(int, input().split())

first = 0
second = 0

for _ in range(n):
    first += input().count("*")

for _ in range(n):
    second += input().count("*")

print(first, second)