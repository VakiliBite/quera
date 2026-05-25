word = input()

a,e,i,o,u = word.count("a") , word.count("e") , word.count("i") , word.count("o") , word.count("u")

sumcount = a + e + i+ o + u

print(2**sumcount)