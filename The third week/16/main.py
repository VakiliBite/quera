from math import sqrt


a , b = input().split()

d = abs(int(a) - int(b))

divisior = []

for i in range(2 , int(sqrt(d)) + 1):
    if d % i == 0 :
        divisior.append(i)
        if i != d // i:
            divisior.append(d//i)
            
if d > 1:
    divisior.append(d)
        
divisior.sort()
print(*divisior , sep=" ")
        
    