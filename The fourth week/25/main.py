S = input().strip()
n = int(input())

count = 0
for _ in range(n):
    t = input().strip()
    
    i = 0
    for ch in t:
        if i < len(S) and ch == S[i]:
            i += 1
        if i == len(S):   
            break
    
    if i == len(S):
        count += 1

print(count)