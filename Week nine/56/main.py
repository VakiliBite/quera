s = input()
t = input()
n = int(input())

if len(s) > n:
    print(-1)
    exit()

if t in s:
    print(-1)
    exit()

for c in ['a', 'b']:
    ans = c * n
    ans = s + ans[len(s):]
    if t not in ans:
        print(ans)
        exit()

print(-1)