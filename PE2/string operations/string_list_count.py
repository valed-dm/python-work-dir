# The list() function takes its argument (a string) and creates a new list containing all the string's characters, one per list element.
# Note: it's not strictly a string function - list() is able to create a new list from many other entities (e.g., from tuples and dictionaries).

# Demonstrating the list() function:
print(list("abcabc"))

# The count() method counts all occurrences of the element inside the sequence. 
# The absence of such elements doesn't cause any problems.

# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))


# Moreover, Python strings have a significant number of methods intended exclusively for processing characters. 
# Don't expect them to work with any other collections. 
# The complete list of is presented here: https://docs.python.org/3.4/library/stdtypes.html#string-methods.

# We're going to show you the ones we consider the most useful.