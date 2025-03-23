import re

text = input()

cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
