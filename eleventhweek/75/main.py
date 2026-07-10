import math

n = int(input())

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

if n % 2 == 1 and is_prime(n):
    print("zoj")
else:
    print("fard")