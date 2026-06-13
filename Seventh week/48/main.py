n, V = map(int, input().split())

juices = []

for _ in range(n):
    h, v = map(int, input().split())
    juices.append((h, v))

juices.sort(key=lambda x: x[0] / x[1], reverse=True)

ans = 0.0
rem = V

for h, v in juices:
    if rem == 0:
        break

    if v <= rem:
        ans += h
        rem -= v
    else:
        ans += h * rem / v
        rem = 0

print(f"{ans:.1f}")