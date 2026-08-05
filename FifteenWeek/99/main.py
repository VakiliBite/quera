a, b = map(int, input().split())

h = (12 - a) % 12
m = (60 - b) % 60

print(f"{h:02d}:{m:02d}")