a = int(input())
b = int(input())

if b >= a :
    print("Wrong order!")

elif (a - b) % 2 == 1 :
    print("Wrong difference!")

else:
    margin = (a - b) // 2
    for i in range(a):
        row = []

        for j in range(a):
            if (margin <= i < margin + b and
                margin <= j < margin + b):
                row.append(" ")
            else:
                row.append("*")

        print(" ".join(row))
