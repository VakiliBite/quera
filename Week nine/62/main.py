l, r = map(int, input().split())

for i in range(l - 1, r):
    print('1' if i.bit_count() % 2 == 0 else '0', end='')