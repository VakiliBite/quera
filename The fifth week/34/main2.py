myword=['a' , 'e' , 'o' , 'u' , 'i']

word = input()
count = 0

for i in word:
    if i in myword:
        count += 1

print(count)
