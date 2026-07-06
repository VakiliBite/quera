import string

text = input().lower()
text = text.translate(str.maketrans('', '', string.punctuation))
text = text.replace(" ", "")

print("YES" if text == text[::-1] else "NO")