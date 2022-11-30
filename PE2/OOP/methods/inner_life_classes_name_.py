# __dict__ is a dictionary. Another built-in property worth mentioning is __name__, which is a string.

# The property contains the name of the class. It's nothing exciting, just a string.

# Note: the __name__ attribute is absent from the object - it exists only inside classes.


# If you want to find the class of a particular object, you can use a function named type(), which is able (among other things) to find a class which has been used to instantiate any object.

# Look at the code in the editor, run it, and see for yourself.

# The code outputs:

# Classy
# Classy
# output

# Note that a statement like this one:

# print(obj.__name__)


# will cause an error.

class Classy:
    pass


print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)
# AttributeError: 'Classy' object has no attribute '__name__'. Did you mean: '__ne__'?
# print(obj.__name__)
