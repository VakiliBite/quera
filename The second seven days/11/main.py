h = int(input())
k = int(input())

if k%2 != 0 or (k%2 != 0 and h%2 !=0) :
    print("NO")
elif h%2 != 0 and k == 0:
    print("NO")
else:
    print("YES")
