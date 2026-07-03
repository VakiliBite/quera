import math 

n , k = map(int , input().split())

result = n

for _ in range(k):
    result /= 2

print(math.floor(result))