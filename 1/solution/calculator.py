def calculate_floor(string):
    result = 0
    
    cal = {
        'U' : 1,
        'D' : -1
    }
    
    us_func = list(string)
    for i in us_func:
        result += (cal[i])
    
    return result
