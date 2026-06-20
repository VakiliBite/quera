def to_base(number, base):

    if number == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while number > 0:
        result = digits[number % base] + result
        number //= base

    return result

number , base = map(int , input().split())

print(to_base(number , base))