n, m = map(int, input().split())
mj_tasks = set(map(int, input().split()))
mostafa_tasks = set(map(int, input().split()))

if mj_tasks == mostafa_tasks:
    print("Both")
elif mj_tasks.issubset(mostafa_tasks) and len(mostafa_tasks) > len(mj_tasks):
    print("Mohammad Javad")
elif mostafa_tasks.issubset(mj_tasks) and len(mj_tasks) > len(mostafa_tasks):
    print("Mostafa")
else:
    print("None")

