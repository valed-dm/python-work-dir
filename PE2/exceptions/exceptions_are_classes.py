# All the previous examples were content with detecting a specific kind of exception and responding 
# to it in an appropriate way. Now we're going to delve deeper, and look inside the exception itself.

# You probably won't be surprised to learn that exceptions are classes. Furthermore, when an exception is raised,
# an object of the class is instantiated, and goes through all levels of program execution, 
# looking for the except branch that is prepared to deal with it.

# Such an object carries some useful information which can help you to precisely identify all aspects of 
# the pending situation. To achieve that goal, 
# Python offers a special variant of the exception clause - you can find it in the editor.

# As you can see, the except statement is extended, and contains an additional phrase starting with the as keyword, 
# followed by an identifier. The identifier is designed to catch the exception object so you can analyze 
# its nature and draw proper conclusions.

# Note: the identifier's scope covers its except branch, and doesn't go any further.

# The example presents a very simple way of utilizing the received object - 
# just print it out (as you can see, the output is produced by the object's __str__() method) and it contains 
# a brief message describing the reason.

# The same message will be printed if there is no fitting except block in the code, 
# and Python is forced to handle it alone.

try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())

# All the built-in Python exceptions form a hierarchy of classes. 
# There is no obstacle to extending it if you find it reasonable.

# Look at the code in the editor.

def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)
