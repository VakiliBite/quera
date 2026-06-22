n = int(input())


winsg = []

for _ in range(n):
    wc = int(input())
    sets = input()[:wc]
    if sets.count("Q") > sets.count("C"):
        winsg.append("Quera")
    else:
        winsg.append("CodeCup")

print(*winsg , sep="\n")