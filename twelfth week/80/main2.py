n = int(input())
A = input().strip()

m = int(input())
O = input().strip()

lcp = 0
while lcp < min(n, m) and A[lcp] == O[lcp]:
    lcp += 1

print(n + m - 2 * lcp)