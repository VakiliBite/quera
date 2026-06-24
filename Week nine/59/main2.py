n = int(input())

def winner(par):


    if par == 1:
        return 1

    if par%2 == 0 :
        result = winner(par//2)
        result = result*2 -1
        if result == 0 :
            result += par
        return result

    if par%2 != 0:
        result = winner(par//2)
        result = result*2 + 1
        if result > par :
            result -= par
        return result

print(winner(n))