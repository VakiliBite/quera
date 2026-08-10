p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())

persepolis = p1 + p2
esteghlal = s1 + s2

if persepolis > esteghlal:
    print("Persepolis")
elif esteghlal > persepolis:
    print("Esteghlal")
else:
    if p2 > s1:
        print("Persepolis")
    elif s1 > p2:
        print("Esteghlal")
    else:
        print("Penalty")