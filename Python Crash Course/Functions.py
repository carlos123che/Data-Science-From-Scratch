def double(x):
    """ This function multipiles its input by 2 """
    return x * 2

def apply_to_one(f):
    """ Calls the function given, with 1 as its argument """
    return f(1)

# Default parameters
def full_name(first = "What's-his-name", last = "Something"):
    return first + " " + last


# Call a funcion
print("-> double Test. Input(5), Result:" + str(double(5)) )

# Assign a function to a variable
my_double = double # Refers to the double function
x = apply_to_one(my_double) 
print("-> apply_to_one Test. Input(double function), Result: "  + str(x) )


# Lambda
y = apply_to_one(lambda x: x + 4)
print("-> apply_to_one lambda Test. Input(y with lambda x: x + 4)), Result: "  + str(y) )

# Fucionts with defaults
print(full_name("Carlos", "Ché"))
print(full_name(last = "Ché"))
print(full_name("Carlos"))
print(full_name())
