import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    out = []
    target = "acpc"
    for i in range(1, t + 1):
        s = data[i]
        if len(s) < 5:
            out.append("NO")
            continue
        it = iter(s)
        if all(c in it for c in target):
            out.append("YES")
        else:
            out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()