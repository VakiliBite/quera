

def calculator(n, m, li):
    myli = li
    newlist = []
    count1 = 0
    indexchose = 0
    
    result = 0
    
    for _ in range(n//m + 1):
        if count1 < n:
            newlist.append(sum(myli[:m]))
            myli = myli[indexchose+m:]
            count1 += m 
        else:
            if len(myli) != 0:
                newlist.append(sum(myli))

            
    for i in range(len(newlist)):
        if i%2 == 0:
            result += newlist[i]

        else:
            result -= newlist[i]
            
    return result
    
    
