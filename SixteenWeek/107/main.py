a = [list(map(int, input().split())) for _ in range(3)]

balance = [0, 0, 0]

for i in range(3):
    for j in range(3):
        if i == j:
            continue

        balance[i] += a[i][j]
        balance[j] -= a[i][j]

ans = [[0] * 3 for _ in range(3)]

debtors = []
creditors = []

for i in range(3):
    if balance[i] > 0:
        debtors.append(i)
    elif balance[i] < 0:
        creditors.append(i)

d = 0
c = 0

while d < len(debtors) and c < len(creditors):
    debtor = debtors[d]
    creditor = creditors[c]

    payment = min(balance[debtor], -balance[creditor])

    ans[debtor][creditor] = payment

    balance[debtor] -= payment
    balance[creditor] += payment

    if balance[debtor] == 0:
        d += 1

    if balance[creditor] == 0:
        c += 1

for row in ans:
    print(*row)