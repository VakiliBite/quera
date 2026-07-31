n = int(input())
k = int(input())
s = list(input())

for _ in range(k):
    s = [s[-1]] + s[:-1]

    for i in range(n):
        if s[i] == 'z':
            s[i] = 'a'
        else:
            s[i] = chr(ord(s[i]) + 1)

print("".join(s))