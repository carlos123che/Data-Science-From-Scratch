
integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]

list_length = len(integer_list) # equals 3
list_sum = sum(integer_list) # equals 6

print(list_length)
print(list_sum)


x = range(10) # is the list [0, 1, ..., 9]
zero = x[0] # equals 0, lists are 0-indexed
one = x[1] # equals 1
nine = x[-1] # equals 9, 'Pythonic' for last element
eight = x[-2] # equals 8, 'Pythonic' for next-to-last element
x[0] = -1 # now x is [-1, 1, 2, 3, ..., 9]


first_three = x[:3] # [-1, 1, 2]
three_to_end = x[3:] # [3, 4, ..., 9]
one_to_four = x[1:5] # [1, 2, 3, 4]
last_three = x[-3:] # [7, 8, 9]
without_first_and_last = x[1:-1] # [1, 2, ..., 8]
copy_of_x = x[:] # [-1, 1, 2, ..., 9]

1 in [1, 2, 3] # True
0 in [1, 2, 3] # False

x = [1, 2, 3]
x.extend([4, 5, 6]) 

#if you dont want to modify x
x = [1, 2, 3]
y = x + [4, 5, 6] 



x = [1, 2, 3]
x.append(0) # x is now [1, 2, 3, 0]


x, y = [1, 2] # now x is 1, y is 2
# although you will get a ValueError if you don’t have the same numbers of elements
# on both sides.
_, y = [1, 2] # now y == 2, didn't care about the first element
print(_)


# TUPLES
x, y = 1, 2 # now x is 1, y is 2
x, y = y, x # Pythonic way to swap variables; now x is 2, y is 1
