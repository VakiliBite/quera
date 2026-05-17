n, m = map(int, input().split())
mapping = {}
for _ in range(n):
    key, val = input().split()
    mapping[key] = val
goat_words = input().split()

response = []
for w in goat_words:
    if w in mapping:
        response.append(mapping[w])
    response.append("kachal!")

print(" ".join(response))