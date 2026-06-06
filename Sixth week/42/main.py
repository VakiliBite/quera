n = int(input())

mycart = [input() for _ in range(n)]

mylist = []
result = []
resultlen = []
for i in mycart:
    mylist=i.split('1')
    for j in mylist:
        if '0' in j:
            result.append(j)
    resultlen.append(len(result))
    result.clear()

print(*resultlen , sep="\n")
    