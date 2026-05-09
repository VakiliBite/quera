us_input = list(map(int , input().split()))

ayamosalas = sum(us_input) == 180
ayasefr = 0 in us_input

if ayamosalas and not ayasefr:
    print("Yes")
else:
    print("No")