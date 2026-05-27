n = int(input())

arr = list(map(int, input().split()))

arr.sort(reverse=True)

h = 0

for i in range(n):
    if arr[i] >= i + 1:
        h = i + 1
    else:
        break

print(h)