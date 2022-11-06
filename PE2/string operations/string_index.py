# The index() method (it's a method, not a function) searches the sequence from the beginning, in order to find the first element of the value specified in its argument.
# Note: the element searched for must occur in the sequence - its absence will cause a ValueError exception.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("my_list index(2) = ", my_list.index(2))

# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))
