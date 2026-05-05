def fib(n):
    
    a , b = 1 , 1
    fibset = {1}
    
    while b <= n:
        a , b = b , a+b
        fibset.add(b)
        
    for i in range(1 , n+1):
        if i in fibset:
            print("+" , end='')
        else:
            print("-" , end='')

    

            
    
c = fib(int(input()))