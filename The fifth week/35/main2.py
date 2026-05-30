ints = []

while True:
    myinput = int(input())
    if myinput == 0:
        break 
    else:
        ints.append(myinput)

ints = reversed(ints)
print(*ints , sep="\n")