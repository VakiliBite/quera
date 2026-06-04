n = int(input())
films = [input() for _ in range(n)]
result = []

for film in films:
    splitfilm=film.split()
    tempfilm = []
    for i in range(len(splitfilm)):
        myfilm = splitfilm[i].lower()
        myfilm = myfilm[0].upper() + myfilm[1:]
        tempfilm.append(myfilm)

    result.append(' '.join(tempfilm))

print(*result , sep="\n")