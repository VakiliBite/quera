x1 , x2 = map(int , input().split())

if x1 > x2:
    print("L"* (x1 - x2))
elif x1 < x2:
    print("R"* (x2 - x1))
else:
    print("Saal Noo Mobarak!")