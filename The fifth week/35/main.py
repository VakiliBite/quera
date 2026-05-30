r1 = input().split()
r2 = input().split()

result = 0


for i in range(8):
    if r1[i] == r2[i] and r1[i] == '1' and r2[i] == '1':
        result += 1



print(result)