n = int(input())
basep = int(input())
lessp = []
result = basep

for _ in range(n-1):
    lessp.append(int(input()))

result += sum(lessp)

print(result)