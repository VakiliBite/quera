n = int(input())

myint = [int(i) for i in str(n)]
resultlist = 0
while True:
    if len(myint) >= 2:
        resultlist = sum(myint)
        myint.clear()
        myint = [int(i) for i in str(resultlist)]
    else:
        resultlist = sum(myint)
        print(resultlist)
        break
    
           