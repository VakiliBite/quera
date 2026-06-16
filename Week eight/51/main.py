n = int(input())

for i in range(n):
    for j in range(2 * n - 1):
        if i == n - 1:
            if j % 2 == 0:
                print("D", end="")
            else:
                print(".", end="")
        elif j == n - 1 - i or j == n - 1 + i:
            print("D", end="")
        else:
            print(".", end="")
    print()