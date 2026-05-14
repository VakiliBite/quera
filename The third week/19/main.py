a , b , c = input().split("?")
a , b , c = int(a) , int(b) , int(c)

result = []
result.append(a * b * c)
result.append(a+b+c)
result.append((a+b)*c)
result.append(a*(b+c))
result.append(a*b+c)
result.append(a+b*c)

print(max(result))