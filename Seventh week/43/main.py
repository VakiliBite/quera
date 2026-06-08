from math import isqrt

q = int(input())

for _ in range(q):
    l, r = map(int, input().split())

    left = isqrt(l)
    if left * left < l:
        left += 1

    right = isqrt(r)

    print(max(0, right - left + 1))