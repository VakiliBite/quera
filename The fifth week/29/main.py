nums = input().split()[:5]
found = False

for i in range(5):
    for p in range(i+1 , 5):
        for j in range(p+1 , 5):
            a , b , c = int(nums[i]) , int(nums[p]) , int(nums[j])
            if a + b > c and a + c > b and b + c > a:
                found = True
                break
        if found:
            break    
    if found:
        break
        
        
if found:
    print("YES")
else:
    print("NO")