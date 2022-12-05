# How to create your own exception
# The exceptions hierarchy is neither closed nor finished, and you can always extend it if you want or need to create your own world populated with your own exceptions.

# It may be useful when you create a complex module which detects errors and raises exceptions, and you want the exceptions to be easily distinguishable from any others brought by Python.

# This is done by defining your own, new exceptions as subclasses derived from predefined ones.

# Note: if you want to create an exception which will be utilized as a specialized case of any built-in exception, derive it from just this one. If you want to build your own hierarchy, and don't want it to be closely connected to Python's exception tree, derive it from any of the top exception classes, like Exception.

# Imagine that you've created a brand new arithmetic, ruled by your own laws and theorems. It's clear that division has been redefined, too, and has to behave in a different way than routine dividing. It's also clear that this new division should raise its own exception, different from the built-in ZeroDivisionError, but it's reasonable to assume that in some circumstances, you (or your arithmetic's user) may want to treat all zero divisions in the same way.

# Demands like these may be fulfilled in the way presented in the editor. Look at the code, and let's analyze it:

# We've defined our own exception, named MyZeroDivisionError, derived from the built-in ZeroDivisionError. As you can see, we've decided not to add any new components to the class.

# In effect, an exception of this class can be - depending on the desired point of view - treated like a plain ZeroDivisionError, or considered separately.

# The do_the_division() function raises either a MyZeroDivisionError or ZeroDivisionError exception, depending on the argument's value.

# The function is invoked four times in total, while the first two invocations are handled using only one except branch (the more general one) and the last two ones with two different branches, able to distinguish the exceptions (don't forget: the order of the branches makes a fundamental difference!)

class MyZeroDivisionError(ZeroDivisionError):
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise ZeroDivisionError("some bad news")


for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division by zero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')

print()

# How to create your own exception: continued
# When you're going to build a completely new universe filled with completely new creatures that have nothing in common with all the familiar things, you may want to build your own exception structure.
# For example, if you work on a large simulation system which is intended to model the activities of a pizza restaurant, it can be desirable to form a separate hierarchy of exceptions.
# You can start building it by defining a general exception as a new base class for any other specialized exception. We've done in in the following way:


class PizzaError(Exception):
    def __init__(self, pizza='unknown', message=''):
        Exception.__init__(self, message)
        self.pizza = pizza
        print(self.pizza, 'error occured --> pizza error: ', end='')


# Note: we're going to collect more specific information here than a regular Exception does,
# so our constructor will take two arguments:
# one specifying a pizza as a subject of the process,
# and one containing a more or less precise description of the problem.

# As you can see, we pass the second parameter to the superclass constructor, and save the first inside our own property.
# A more specific problem (like an excess of cheese) can require a more specific exception.
# It's possible to derive the new class from the already defined PizzaError class, like we've done here:

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='unknown', cheese='>100', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese
        print('cheese error: ', end='')


# The TooMuchCheeseError exception needs more information than the regular PizzaError exception,
# so we add it to the constructor - the name cheese is then stored for further processing.

def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20), ('frankie', 160)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
    finally:
        print('Bye!')