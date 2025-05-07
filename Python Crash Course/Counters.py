from collections import Counter
c = Counter( [ 0, 1, 2, 0])
print(c)

document = [ "casa", "carro", "raton", "casa", "casa", "carro", "leon"]
word_counts = Counter(document)
print(word_counts)

# print the 2 most common words and their counts
for word, count in word_counts.most_common(2):
    print(word, count)
