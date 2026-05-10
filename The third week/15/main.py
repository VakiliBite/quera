s = input()

def s_validate(s):
    
    my_list = []
    for i in s:
        if i != "=":
            my_list.append(i)
        else:
            my_list = my_list[0:len(my_list)-1]
            continue
            
    print(*my_list , sep="")

s_validate(s)