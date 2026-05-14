def prime_factorization(n):
    i = 2
    factors = {}
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    
    parts = []
    for base, exp in factors.items():
        if exp == 1:
            parts.append(str(base))
        else:
            parts.append(f"{base}^{exp}")
    
    return "*".join(parts)

num = int(input())
print(f"{prime_factorization(num)}")  