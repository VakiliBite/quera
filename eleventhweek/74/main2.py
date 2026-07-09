all_days = {"shanbe", "1shanbe", "2shanbe", "3shanbe", "4shanbe", "5shanbe", "jome"}

busy_days = set()

for _ in range(3):
    n = int(input()) 
    days = input().split() 
    for day in days:
        busy_days.add(day)

free_days = all_days - busy_days

print(len(free_days))