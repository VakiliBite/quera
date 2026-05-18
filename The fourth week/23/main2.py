my_captal_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
my_small_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

result = []

mywords = input()
for i in mywords:
    if i.isupper():
        ai = my_captal_list.index(i)
        xi1 = mywords.count(i.upper())
        xi2 = mywords.count(i.lower())
        xi = xi1 + xi2
        y = (xi*ai + 1) % 26
        result.append(my_captal_list[y])
    else: 
        ai = my_small_list.index(i)
        xi1 = mywords.count(i.upper())
        xi2 = mywords.count(i.lower())
        xi = xi1 + xi2
        y = (xi*ai + 1) % 26
        result.append(my_small_list[y])
        
print(''.join(result))