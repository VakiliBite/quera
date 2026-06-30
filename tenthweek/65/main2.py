word = input()

result = "khoob"

for i in word:
    if word.count(i) % 2 != 0:
        result = "bad"
        break
    else:
        pass 

print(result)