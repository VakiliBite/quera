import sys

data = sys.stdin.buffer.read().split()
it = iter(data)
t = int(next(it))
out = []
for _ in range(t):
    s = int(next(it))
    x = 0
    for __ in range(s):
        a = next(it)
        b = next(it)
        if a == b'buy_one' and b == b'buy_one':
            x += 1
        elif a == b'copy_paste' and b == b'copy_paste':
            x *= 2
        else:
            x = max(x + 1, x * 2)
    out.append(str(x))
sys.stdout.write("\n".join(out))