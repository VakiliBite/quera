from math import factorial

result = 0

a ,x ,n = map(int , input().split())

def C(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

for i in range(n + 1):
    result += C(n,i)* x**i * a**(n-i)

print(result)
    