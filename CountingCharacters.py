text = input("")

char_count = {}

for char in text:
    if char not in char_count:
        char_count[char] = 1
    else:
        char_count[char] += 1

for char in char_count:
    print(f"{char}={char_count[char]}")
