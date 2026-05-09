a = int(input())
b = int(input())
c = int(input())

mylist = [a , b , c]
getmax = max(mylist)
mylist.remove(max(mylist))

equal = mylist[0]**2 + mylist[1]**2 == getmax**2

if equal:
    print("YES")
else:
    print("NO")


    
