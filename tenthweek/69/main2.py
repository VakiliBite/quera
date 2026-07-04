import math

a = int(input())
b = int(input())

result = []

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0 :
        return False

    for i in range(2 , int(math.sqrt(number)) + 1):
        if number % i == 0 :
            return False

    return True

for i in range(a + 1 , b):
    if is_prime(i):
        result.append(i)


print(*result , sep=',')
        