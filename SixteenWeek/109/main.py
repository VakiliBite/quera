s = input().strip()

ans = 1

for ch in s:
    if ch in "TDFL":
        ans *= 2

print(ans)