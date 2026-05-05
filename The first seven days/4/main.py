import math 

us_input = int(input())

input_list = [int(input()) for i in range(us_input)]

lcm = math.lcm(*input_list) + 1

lcmresult = lcm // 30

result = lcm - (lcmresult * 30) 

print(result)



    
