n , x , y = input().split()
n, x , y = int(n) , int(x) , int(y)
nresult = "-1"
result = []

for a in range(0 , (n//x)+1):
    baghimande = n - a*x
    
    if baghimande%y == 0:
        b = baghimande // y 
        result.append(str(a))
        result.append(str(b))
        
print(' '.join(result) if len(result)>0 else nresult)
        
