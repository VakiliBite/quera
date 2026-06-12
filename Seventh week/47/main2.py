n = int(input())

numbers = [input() for _ in range(n)]

def validate1(number):
    for i in number:
        if number.count(i)>=4:
            return True

    return False
        
        

def validate2(number):

    cnt = 1

    for i in range(1 , len(number)):
        if number[i] == number[i-1]:
            cnt += 1 
            if cnt >= 3:
                return True

        else:
            cnt = 1

    return False
        

def validate3(number:str):
    if number[::-1]==number:
        return True

    return False


for number in numbers:
    if validate1(number) or validate2(number) or validate3(number):
        print("Ronde!")
    else:
        print("Rond Nist")

