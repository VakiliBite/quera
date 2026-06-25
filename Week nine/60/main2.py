result = []

for _ in range(2):
    n = int(input())
    k = int(input())
    result.append(max([n , k]) - min([n , k]))

if result[0] == result[1]:
    print("Equal")
elif result[0] > result[1]:
    print("Shekarestan")
else:
    print("Namakestan")