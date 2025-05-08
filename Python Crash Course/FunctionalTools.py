from functools import partial, reduce


def exp(base, power):
 return base ** power


# def two_to_the(power):
#  return exp(2, power)

two_to_the = partial(exp, 2) # is now a function of one variable
print(two_to_the(3)) # 8

square_of = partial(exp, power=2)
print(square_of(3))  # 9

def double(x):
 return 2 * x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs] # [2, 4, 6, 8]
print(twice_xs)
twice_xs = map(double, xs) # same as above
print(twice_xs)
list_doubler = partial(map, double) # *function* that doubles a list
print(list_doubler)
twice_xs = list_doubler(xs) # again [2, 4, 6, 8]
print(twice_xs)


def multiply(x, y): return x * y
products = map(multiply, [1, 2], [4, 5]) # [1 * 4, 2 * 5] = [4, 10]
print(list(products))


def is_even(x):
 """True if x is even, False if x is odd"""
 return x % 2 == 0

x_evens = [x for x in xs if is_even(x)] # [2, 4]
x_evens = filter(is_even, xs) # same as above
list_evener = partial(filter, is_even) # *function* that filters a list
x_evens = list_evener(xs) # again [2, 4]

x_product = reduce(multiply, xs) # = 1 * 2 * 3 * 4 = 24
list_product = partial(reduce, multiply) # *function* that reduces a list
x_product = list_product(xs) # again = 24