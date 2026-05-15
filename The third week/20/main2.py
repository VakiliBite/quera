def normalize(phone):
    if phone.count('+') > 1 or ('+' in phone and not phone.startswith('+')):
        return "invalid"

    digits = [ch for ch in phone if ch.isdigit()]
    
    if phone.startswith('09') and len(digits) == 11:
        return '+98' + ''.join(digits[1:])
    
    if phone.startswith('98') and len(digits) == 12:
        return '+98' + ''.join(digits[2:])
    
    if phone.startswith('+98') and len(phone) == 13 and phone[1:].isdigit():
        return phone
    
    return "invalid"

def main():
    n = int(input().strip())
    for _ in range(n):
        s = input()
        print(normalize(s))

main()