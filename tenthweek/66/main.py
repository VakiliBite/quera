p, d = map(int, input().split())

x = d
while x % p > p // 2:
    x += d

print(x)