a , b = map(int , input().split())

if a == 0 and b != 0:
    print("invalid")
elif a == 0 and b == 0:
    print("infinite")
else:
    print("unique")