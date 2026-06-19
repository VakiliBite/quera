from collections import Counter


n = int(input())

sina = Counter()

for _ in range(n):
    sina[input()] += 1

for _ in range(n-1):
    sina[input()] -= 1

for name , count in sina.items():
    if count > 0:
        print(name)
        break