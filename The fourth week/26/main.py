n = int(input())

mlist = []
result = []

for i in range(n):
    s , c = input().split()
    mlist.append((s,c))
    
for x , y in mlist:
    result.append(int(x)*int(y))
        
print(sum(result))
    