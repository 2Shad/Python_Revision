text = "this is a test. this test is just a test."
#####################################################
word_counts = dict()
duplicate = set()
for word in text.split():
    word = word.strip(".,").lower()
    word_counts[word] = word_counts.get(word, 0) + 1
    if word_counts[word] > 1:
        duplicate.add(word)
for word in duplicate:
    print(f'{word}: {word_counts[word]}')