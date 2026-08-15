import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = 4 * k

    a = list(map(int, input().split()))

    b = a + a[:k]

    pref = [0] * (len(b) + 1)

    for i in range(len(b)):
        pref[i + 1] = pref[i] + b[i]

    sums = []

    for i in range(n):
        sums.append(pref[i + k] - pref[i])

    mn = min(sums)
    mx = max(sums)

    ans = False

    for i in range(n):
        summer = sums[i]
        winter = sums[(i + 2 * k) % n]

        if summer == mn and winter == mx:
            ans = True
            break

    print("Yes" if ans else "No")