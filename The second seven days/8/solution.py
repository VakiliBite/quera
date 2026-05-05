import math
def get_func(ls):
    
    func_list = []
    
    for i in ls:
        if i == "square":
            func_list.append(lambda zl : zl**2)
        elif i == "circle":
            func_list.append(lambda sho : math.pi*sho**2)
        elif i == "rectangle":
            func_list.append(lambda tol , arz : tol*arz)
        elif i == "triangle":
            func_list.append(lambda gha , ert :(gha*ert)/2)
        else:
            pass
            
    return func_list
    

        
