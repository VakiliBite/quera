n = int(input())
status = [int(input()) for _ in range(n)]

pervious = None
count = 0

for i in status:
    if pervious is None:
        pervious = i 
    elif pervious != i:
        count += 1
        pervious = i

print(count)