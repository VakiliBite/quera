t = int(input())

for _ in range(t):
    n, t1, t2 = map(int, input().split())
    print(n * t1 + (n - 1) * t2)
    