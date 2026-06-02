word = input()

result = []

for i in range(len(word)):
    result.append(word[i]*i)


for i in range(len(result)):
    print(result[i]+word[i:])

