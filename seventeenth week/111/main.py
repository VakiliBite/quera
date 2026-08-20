n = int(input())

for a in range(1, n // 3 + 1):
    numerator = n * n - 2 * n * a
    denominator = 2 * (n - a)

    if numerator > 0 and numerator % denominator == 0:
        b = numerator // denominator
        c = n - a - b

        if a < b < c and a * a + b * b == c * c:
            print(a, b, c)
            break
else:
    print("Impossible")