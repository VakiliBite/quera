n = int(input())

result = []

for _ in range(n):
    x , v = map(int , input().split())
    result.append(x/v)

print(min(result))