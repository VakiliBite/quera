n  , jayegol = input().split()

livan = ['0'] * 3

pos = {
    "L" : 0,
    "M" : 1,
    "R" : 2
}

gol = jayegol

livan[pos[jayegol]] = '1'

for i in range(int(n)): 
    newpos , oldpos = input().split()
    livan[pos[newpos]] , livan[pos[oldpos]] = livan[pos[oldpos]] , livan[pos[newpos]]

for key , value in pos.items():
    if livan[value] == '1':
        gol = key 

print(gol)
