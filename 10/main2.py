from functools import reduce
from math import gcd

n = int(input())
k = list(map(int , input().split()[:n]))

gcd_result = reduce(gcd , k)
k_new = [i//gcd_result for i in k]
result = reduce(lambda x,y : y+x , k_new)

print(result)


