from unittest import result


def valid(code):
    s = list(map(int, code))
    c = 0
    for i in range(9):
        c += (10 - i) * s[i]
    c %= 11

    if c <= 1:
        return s[9] == c
    else:
        return s[9] == 11 - c


t = int(input())
result = []

for _ in range(t):
    code = list(input().strip())
    pos = code.index('?')

    ans = []

    for d in "0123456789":
        code[pos] = d
        candidate = "".join(code)
        if valid(candidate):
            ans.append(candidate)

    if len(ans) == 0:
        result.append("cannot be recovered!")

    elif len(ans) == 1:
        result.append(ans[0])

    else:
        result.append("it's not unique!")

print(*result , sep="\n")

