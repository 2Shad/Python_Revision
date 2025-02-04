word = "Racecar"
#######################
word = word.lower()
i = 0
lenght = len(word) - 1

while i < (lenght / 2):
    if word[i] != word[(lenght-i)]:
        print('not palindrome')
        break
    i += 1
else:
    print('palindrome')