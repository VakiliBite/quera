n, x, k = map(int, input().split())

shab = [input() for _ in range(n)]

ans = (x - 1 + k) % n

print(shab[ans])