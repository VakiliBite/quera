n = int(input())

mylist = [input() for _ in range(n)]
result = []

for i in mylist:
    tempset = set(i)
    result.append(len(tempset))

print(max(result))