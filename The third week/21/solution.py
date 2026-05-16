myfruits = tuple()


def fruits(fruit_list:tuple):
    result = dict()
    for fruit in fruit_list:
        if fruit["shape"] == "sphere" and 300<=fruit["mass"]<=600 and 100<=fruit["volume"]<=500:
            name = fruit["name"]
            result[name] = result.get(name , 0) + 1
    return result
        
