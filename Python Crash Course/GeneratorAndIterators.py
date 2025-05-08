# A generator is something you can iterate over , but whose values are produced as needed
# first way of using generators is with  yield
def lazy_range(n):
 """a lazy version of range"""
 i = 0
 while i < n:
    yield i
    i += 1

for i in lazy_range(10):
 do_something_with(i) # the following loop will consume the values one at a time


# You should iterate without a break but yes you can manke an infinite list
def natural_numbers():
 """returns 1, 2, 3, ..."""
 n = 1
 while True:
    yield n
    n += 1

#The flip side of laziness is that you can only iterate through a gen‐
#erator once. If you need to iterate through something multiple
#times, you’ll need to either recreate the generator each time or use a
#list.


# Second way of create generatos is by using for comprehensions wrapped in paren‐
#theses
lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

#Recall also that every dict has an items() method that returns a list of its key-value
#pairs. More frequently we’ll use the iteritems() method, which lazily yields the
#key-value pairs one at a time as we iterate over it.