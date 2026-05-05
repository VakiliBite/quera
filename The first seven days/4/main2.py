us_input = int(input())

def fib(n):
    if n == 1 or n == 0:
        return 1
    return fib(n-1) + fib(n-2)
    
print(fib(us_input))