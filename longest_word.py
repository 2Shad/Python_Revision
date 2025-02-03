sentence = "The quick brown fox jumps over the lazy dog"
###########################################
length = 0
longest_word = ''
for word in sentence.split():
    if len(word) > length:
        length = len(word)
        longest_word = word
print(f"{longest_word}, {length}")
