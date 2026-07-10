def check_mod(number , a , b , c , d):

    if number % a == 0 or number % b == 0 or number % c == 0 or number % d == 0:
        return True

    return False

n , a , b  , c  , d = map(int , input().split())

count = 0
for i in range(1 , n+1):
    if check_mod(i , a , b , c ,d):
        count += 1


print(count)
        