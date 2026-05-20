from math import factorial


x = int(input())
n = int(input())

result = [float(1)]

sum_result = 0

for i in range(1,n):
    mathethic= (x**i)/factorial(i)
    result.append(float(mathethic))
   
print(f"{sum(result):.3f}")