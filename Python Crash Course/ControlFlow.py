if 1 > 2:
 message = "if only 1 were greater than two..."
elif 1 > 3:
 message = "elif stands for 'else if'"
else:
 message = "when all else fails use else (if you want to)"

print(message)

# ternary if
x = 5
parity = "even" if x % 2 == 0 else "odd"
print(parity)


x = 0
while x < 5:
 print( x, "is less than 10")
 x += 1


for x in range(4):
 print( x, "is less than 10")


#break and continue
for x in range(10):
 if x == 3:
    continue # go immediately to the next iteration
 if x == 5:
    break # quit the loop entirely
 print(x)


s = "s"
first_char = s and s[0] 
#since and returns its second value when the first is “truthy,” the first value when it’s not.


x = None
safe_x = x or 0  # safe_x = 0

x = 5
safe_x = x or 0  # safe_x = 5


all([True, 1, {3}])  # True: todos los elementos son truthy (incluido el set {3})
all([True, 1, {}])   # False: el diccionario vacío {} es falsy

any([True, 1, {}])   # True: aunque {} es falsy, los otros dos son truthy

all([])  # True: no hay ningún elemento falsy, así que devuelve True por convención
any([])  # False: no hay ningún elemento truthy, así que devuelve False
