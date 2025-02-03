text = "hello world"
##############################################
letter_count = dict()
for letter in text:
    if letter not in [",", ".", " "]:
        letter = letter.lower()
        letter_count[letter] = letter_count.get(letter, 0) + 1

print(letter_count)