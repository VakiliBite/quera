TAS = {
    '1' : '6',
    '2' : '5',
    '3' : '4',
}

def tas_validate(data):
    for key , value in TAS.items():
        if data != key :
            if data != value:
                continue
            else:
                return key
        else:
            return value

print(tas_validate(input()))