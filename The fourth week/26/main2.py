n = int(input())

result = []
intlist = []

for i in range(1 , n+1):
    if i < n:
        result.append(str(i))
        intlist.append(i)
        result.append(" + ")
    else:
        intlist.append(i)
        result.append(str(i))
        result.append(" =")
    
print(''.join(result) , sum(intlist))