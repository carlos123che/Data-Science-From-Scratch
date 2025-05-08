x = [4,1,2,3]
y = sorted(x) # is [1,2,3,4], x is unchanged
x.sort() # now x is [1,2,3,4]

print(y)

#By default, sort (and sorted) sort a list from smallest to largest b
#If you want elements sorted from largest to smallest, you can specify a reverse=True
# And instead of comparing the elements themselves, you can compare the
# results of a function that you specify with key:

z = sorted([-4,1,-2,3], reverse=True) # is [-4,3,-2,1]
x = sorted([-4,1,-2,3], key=abs, reverse=True) # is [-4,3,-2,1]
print(z)
print(x)


word_counts = {'hello': 5, 'world': 2, 'python': 8}
wc = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
print(wc)