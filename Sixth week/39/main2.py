a, b, c, d, e, f = map(int, input().split())

box_small = min(a, b)
box_big = max(a, b)

sides = [(d, e), (d, f), (e, f)]

for x, y in sides:
    ice_small = min(x, y)
    ice_big = max(x, y)

    if ice_small <= box_small and ice_big <= box_big:
        print("zende mimuni")
        break
else:
    print("dari mimiri")