avali = int(input())
dovomi = int(input())

avali_big = avali%10 > dovomi%10
mosavi = avali%100 == dovomi%100
avali_big2 = avali%10 == dovomi%10 and avali%100 > dovomi%100
if avali_big:
    print(f"{dovomi} < {avali}")
elif mosavi:
    print(f"{dovomi} = {avali}")
elif avali_big2:
    print(f"{dovomi} < {avali}")
else:
    print(f"{avali} < {dovomi}")


