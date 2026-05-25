n = int(input())

names = [input() for _ in range(n)]

first_name_list = []
countable = []

for i in names:
    fullname_split = i.split()
    first_name_list.append(fullname_split[0])
    
for j in first_name_list:
    countable.append(first_name_list.count(j))
    
print(max(countable))
    