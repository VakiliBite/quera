n , q , p = input().split()
Y = set()
N = set()

for i in range(int(n)):
    binary , ny = input().split()
    binary = binary[:int(p)]
    if ny == "Y":
        Y.add(binary)
    elif ny == "N":
        N.add(binary)
      
result = []  
for i in range(int(q)):
    us_input = input()
    
    if us_input in Y:
        result.append("Y")
    elif us_input in N:
        result.append("N")
    else:
        result.append("Unknown")

print(*result,sep="\n")
    




