def is_prime(number):

    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3 , int(number ** 0.5)+1 , 2):
            if number % i == 0:
                return False
        return True

a = int(input())
b = int(input())

result = []

for i in range(a , b+1):
    if is_prime(i):
        result.append(i)

print(*sorted(result) , sep="\n")