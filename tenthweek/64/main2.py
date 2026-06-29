import math

eps = 1e-9

a = float(input())
b = float(input())
c = float(input())

if abs(a) < eps:
    if abs(b) < eps:
        print("IMPOSSIBLE")
    else:
        x = -c / b
        if abs(x) < eps:
            x = 0.0
        print(f"{x:.3f}")
else:
    d = b * b - 4 * a * c

    if d < -eps:
        print("IMPOSSIBLE")
    elif abs(d) < eps:
        x = -b / (2 * a)
        if abs(x) < eps:
            x = 0.0
        print(f"{x:.3f}")
    else:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)

        if abs(x1) < eps:
            x1 = 0.0
        if abs(x2) < eps:
            x2 = 0.0

        if x1 > x2:
            x1, x2 = x2, x1

        print(f"{x1:.3f}")
        print(f"{x2:.3f}")