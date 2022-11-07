# Demonstrating the capitalize() method:
print('aBcD'.capitalize())

# The capitalize() method does exactly what it says - it creates a new string filled with characters taken from the source string, 
# but it tries to modify them in the following way:

# if the first character inside the string is a letter 
# (note: the first character is an element with an index equal to 0, not just the first visible character), 
# it will be converted to upper-case;
# all remaining letters from the string will be converted to lower-case.
# Don't forget that:

# the original string (from which the method is invoked) is not changed in any way 
# (a string's immutability must be obeyed without reservation)
# the modified (capitalized in this case) string is returned as a result 
# - if you don't use it in any way (assign it to a variable, or pass it to a function/method) it will disappear without a trace.
# Note: methods don't have to be invoked from within variables only. 
# They can be invoked directly from within string literals. 
# We're going to use that convention regularly - it will simplify the examples, 
# as the most important aspects will not disappear among unnecessary assignments.

print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())
