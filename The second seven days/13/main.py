us_input = input()

reverse_input = list(reversed([i for i in us_input]))
org_input = [i for i in us_input]

if reverse_input == org_input:
    print("YES")
else:
    print("NO")