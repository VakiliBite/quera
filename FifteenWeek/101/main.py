n = int(input())
a = input()
b = input()

mistakes = 0

for i in range(n):
    if a[i] != b[i]:
        mistakes += 1

print(mistakes)