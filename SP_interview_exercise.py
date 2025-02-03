# From the array text, find the most common word, and output it like "word, 5"
text = ["Extremity, sweetness difficult behaviour he of. On disposal of as landlord horrible. Afraid at highly months do things on at. Situation recommend objection do intention so questions. As greatly removed calling pleased improve an. Last ask him cold feel met spot shy want. Children me laughing we prospect answered followed. At it went is song that held help face.", "Sitting mistake towards his few country ask. You delighted two rapturous six depending objection happiness something the. Off nay impossible, dispatched partiality unaffected. Norland adapted put ham cordial. Ladies talked may shy basket narrow see. Him she distrusts questions sportsmen. Tolerably pretended neglected on my earnestly by. Sex scale sir style truth ought.", "Silent sir say desire fat him letter. Whatever settling goodness too and honoured she building answered her. Strongly thoughts remember mr to do consider debating. Spirits musical behaved on we he farther letters. Repulsive he he as deficient newspaper dashwoods we. Discovered her his pianoforte insipidity entreaties. Began he at terms meant as fancy. Breakfast arranging he if furniture we described on. Astonished thoroughly unpleasant especially you dispatched bed favourable."]
###################################
###################################
words = []
for i in text:
    for word in list(i.split()):
        if word[-1] in [",", "."]:
            word = word[0:len(word)-1]
        words.append(word.lower())


golden_freq = 0
golden_word = ''

for word in words:
    if words.count(word) > golden_freq:
        golden_freq = words.count(word)
        golden_word = word

print(f"{golden_word}, {golden_freq}")