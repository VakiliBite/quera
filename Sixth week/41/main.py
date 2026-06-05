roz = input()

days = {
    'perspolis' : ['shanbe' , 'doshanbe','chaharshanbe'],
    'bahman' : ['yekshanbe' , 'seshanbe' , 'panjshanbe'],
    'jome' : 'tatil'
}

for key , value in days.items():
    if roz in value:
        print(key)
        break
    elif roz == 'jome':
        print(days['jome'])
        break