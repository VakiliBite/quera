a = input().strip()
b = int(input())
c = int(input())

x = 0

for digit in a:
    x = x * b + int(digit)

digits = []

if x == 0:
    digits.append('0')
else:
    while x > 0:
        digits.append(str(x % c))
        x //= c

if digits == digits[::-1]:
    print("YES")
else:
    print("NO")