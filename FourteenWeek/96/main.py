n = int(input())

doc_bit = {
    "0": ["***", "*.*", "***"],
    "1": [".*.", ".*.", ".*."]
}

s = input()

rows = ["", "", ""]

for ch in s:
    for i in range(3):
        rows[i] += doc_bit[ch][i]

for row in rows:
    print(row)