n = int(input())
myl = list(map(int , input().split()[:n]))

print(f"{max(myl):.6f}")