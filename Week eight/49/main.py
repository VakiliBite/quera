import math

mylist = [int(input()) for _ in range(4)]



print(f"""Sum : {sum(mylist):.6f}
Average : {sum(mylist)/len(mylist):.6f}
Product : {math.prod(mylist):.6f}
MAX : {max(mylist):.6f}
MIN : {min(mylist):.6f}""")