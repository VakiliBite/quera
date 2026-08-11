n = int(input())

keys = list(map(int, input().split()))
lamps = list(map(int, input().split()))

answer = []

for i in range(n):
    if lamps[i] == 1:
        answer.append(keys[i])

answer.sort()

print(*answer)