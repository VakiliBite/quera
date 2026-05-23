n = int(input())

result = []
caps = False
for _ in range(n):
    minput = input()
    if minput == "CAPS":
        if caps:
            caps = False
        else:
            caps = True
        
    if caps:
        if minput == "CAPS":
            pass
        else:
            result.append(minput.upper())
    else:
        if minput == "CAPS":
            pass
        else:
            result.append(minput)
        
print(''.join(result))