def game(number):
    result = 0
    int_list = [i for i in str(number)]
    pervios_num = 0
    
    for i in int_list:
        if pervios_num == 0:
            pervios_num = i
        else:
            result = abs(int(i) - int(pervios_num))
        
    
    
    return result