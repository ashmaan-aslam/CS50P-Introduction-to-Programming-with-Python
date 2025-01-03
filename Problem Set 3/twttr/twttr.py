text = input(str("Input: "))
new_text = ""

for char in text:
    if char not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        new_text += char

print(new_text)
