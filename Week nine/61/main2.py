n = int(input())
m = int(input())
a = int(input())
b = int(input())

def get_result(x,y):
    return (x + y - 1) // y


print(min([
    get_result(n , a),
    get_result(n , b),
    get_result(m , a),
    get_result(m , b)
]))