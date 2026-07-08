a , b , l = map(int , input().split())

result = 0

for i in range(1 , l+1):
    if i%2 == 0:
        result += b
    else:
        result += a

print(result)