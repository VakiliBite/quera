r, c = map(int, input().split())

row = 11 - r

if c <= 10:
    print("Right", row, c)
else:
    print("Left", row, 21 - c)