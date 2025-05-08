from collections import defaultdict

document = [ "casa", "carro", "raton", "casa", "casa", "carro", "leon"]


# word_counts = {}
# for word in document:
#  if word in word_counts:
#      word_counts[word] += 1
#  else:
#     word_counts[word] = 1


# word_counts = {}
# for word in document:
#  try:
#     word_counts[word] += 1
#  except KeyError:
#     word_counts[word]


# word_counts = {}
# for word in document:
#  previous_count = word_counts.get(word, 0)
#  word_counts[word] = previous_count + 1

word_counts = defaultdict(int) # int() produces 0
for word in document:
    word_counts[word] += 1

print(word_counts)


dd_list = defaultdict(list) # list() produces an empty list
dd_list[2].append(1)        # now dd_list contais {2: [1]}
print(dd_list)


dd_dict = defaultdict(dict)          # dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seatle"   # {"Joel" : {"City": Seattle"}}
print(dd_dict)

dd_pias = defaultdict(lambda: [ 0, 0])
dd_pias[2][1] = 1                        # now dd_pair contains {2: [0, 1]}
print(dd_pias)