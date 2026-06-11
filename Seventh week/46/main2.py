n , m = map(int , input().split())

p1=[False] * 31
p2=[False] * 31
count = 0

for _ in range(n):
    l , r = map(int , input().split())
    for roz in range(l , r+1):
        p1[roz] = True

for _ in range(m):
    l , r = map(int , input().split())
    for roz in range(l , r+1):
        p2[roz] = True

for rozha in range(1 , 31):
   if p1[rozha] and p2[rozha]:
      count += 1
     
print(count) 