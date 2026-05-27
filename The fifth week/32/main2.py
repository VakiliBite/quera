fasl = input()

mydict = {
    "spring" : ['september', 'october', 'november'],
    "summer":['december', 'january', 'february'],
    "autumn":['march', 'april', 'may'],
    "winter":['june', 'july', 'august']
}

result = ''

for key , value in mydict.items():
    if fasl in value:
        result = key
        
print(result)