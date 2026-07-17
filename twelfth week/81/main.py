a , b = input().split()

c , d = input().split()
if (a == b or c == d) or (a == d or b == c):
   print("YES")
else:
   print("NO") 