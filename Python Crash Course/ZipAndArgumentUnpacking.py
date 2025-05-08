list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2) # is [('a', 1), ('b', 2), ('c', 3)]
#If the lists are different lengths, zip stops as soon as the first list ends.
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

def add(a, b): return a + b
add(1, 2) # returns 3
add([1, 2]) # TypeError!
add(*[1, 2]) # returns 3