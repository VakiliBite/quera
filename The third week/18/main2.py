from types import NoneType


us_input = input()

myhome = [
    [0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0]
]


radif = 1
soton = 0
def validate_list():
    if soton > 8 or radif > 1 or radif < 0:
        return None
    return 1



result = 0 
for i in us_input:

        if i =="L":
                radif -= 1
                soton += 1
                result = validate_list()
                if result is not None:
                    myhome[radif][soton] = 1
                else:
                    print("DEATH")
                    break
    
        elif i == "F":
                soton += 1
                result = validate_list()
                if result is not None:
                    myhome[radif][soton] = 1
                else:
                    print("DEATH")
                    break
        else:
                radif += 1
                soton += 1
                result = validate_list()
                if result is not None:
                    myhome[radif][soton] = 1
                else:
                    print("DEATH")
                    break

if  result is not None:
    for i in myhome:
        
        print(''.join(map(str , i)))