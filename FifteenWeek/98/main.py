t = int(input())

for _ in range(t):
    a, b, h = map(int, input().split())

    if a >= h:
        print(1)
    else:
        days = (h - a + (a - b) - 1) // (a - b) + 1
        print(days)