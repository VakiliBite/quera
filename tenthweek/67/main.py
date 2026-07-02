n = int(input())

result = 0

for i in range(1 , n):
    if n % i == 0:
        result += i

print("YES" if result == n else "NO")
    