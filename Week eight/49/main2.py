a , b , c = map(int , input().split())

T = (a + b + c) // 3


if a == b == c:
    print(0)

elif a == T or b == T or c == T:
    print(1)

else:
    print(2)