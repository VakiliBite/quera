m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())

months = [31] * 6 + [30] * 5 + [29]

day1 = sum(months[:m1 - 1]) + d1
day2 = sum(months[:m2 - 1]) + d2

print(abs(day1 - day2))