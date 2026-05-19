a, b = map(int, input().split())
digits = []
if a == 0:
    digits = [0]
else:
    while a > 0:
        digits.append(a % b)
        a //= b
    digits.reverse()   

sum1 = sum(digits[i] for i in range(0, len(digits), 2))  
sum2 = sum(digits[i] for i in range(1, len(digits), 2)) 

print("Yes" if sum1 == sum2 else "No")

