n, m = map(int, input().split())

top = ' ' + ('_ ' * (m - 1)) + '_'
print(top)

for _ in range(n):
    print('|' + (' |' * m))
    print(top)