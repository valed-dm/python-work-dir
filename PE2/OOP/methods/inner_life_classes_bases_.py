# __bases__ is a tuple. The tuple contains classes (not class names) which are direct superclasses for the class.

# The order is the same as that used inside the class definition.

# We'll show you only a very basic example, as we want to highlight how inheritance works.

# Moreover, we're going to show you how to use this attribute when we discuss the objective aspects of exceptions.

# Note: only classes have this attribute - objects don't.

# We've defined a function named printbases(), designed to present the tuple's contents clearly.

# Look at the code in the editor. Analyze it and run it. It will output:

# ( object )
# ( object )
# ( SuperOne SuperTwo )
# output

# Note: a class without explicit superclasses points to object (a predefined Python class) as its direct ancestor.

class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)
