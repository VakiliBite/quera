words = list(input())

if words.count("R") >=3 or (words.count("Y") >= 2 and words.count("R") >= 2) or (words.count("G") == 0):
    print("nakhor lite")
else:
    print("rahat baash")