n = int(input())
majik = input().split()[:n]

mydict = {}

for i in majik:
    if len(mydict) == 0 :
        mydict[i] = 1
    else:
        if mydict.get(i , False):
            mydict[i] += 1
        else:
            mydict[i] = 1

min = 0
mkey = 0
for key , value in mydict.items():
    if min == 0 :
        min = value
        mkey = key
    if min > value:
        min = value
        mkey = key
    elif min == value:
        if int(mkey) > int(key):
            mkey = key

print(mkey)

    
        