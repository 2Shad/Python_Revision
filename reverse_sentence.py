sentence = "Python is awsome."
#####################
reverse = sentence.split()
reverse.reverse()
reverse[0] = reverse[0][0:len(reverse[0])-1].capitalize()
reverse[-1] = (reverse[-1] + '.').lower()
print(' '.join(reverse))