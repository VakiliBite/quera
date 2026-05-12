
def compress(s):
    if not s:
        return ""
    result = []
    prev = s[0]
    count = 1
    for ch in s[1:]:
        if ch == prev:
            count += 1
        else:
            result.append(prev)
            if count > 1:
                result.append(str(count))
            prev = ch
            count = 1
    result.append(prev)
    if count > 1:
        result.append(str(count))
    return "".join(result)


def decompress(s):
    result = []
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        if ch.isalpha():
            i += 1
            num_str = ""
            while i < n and s[i].isdigit():
                num_str += s[i]
                i += 1
            num = int(num_str) if num_str else 1
            result.append(ch * num)
        else:
            i += 1
    return "".join(result)


def main():
    n = int(input().strip())
    for _ in range(n):
        typ = input().strip()
        word = input().strip()
        if typ == "1":
            print(compress(word))
        else:
            print(decompress(word))


main()
