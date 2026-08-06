import re

sentence = input().lower()
word = input().strip().lower()

reverse_word = word[::-1]

pattern = r'\b(?:' + re.escape(word) + r'|' + re.escape(reverse_word) + r')\b'

print(len(re.findall(pattern, sentence)))