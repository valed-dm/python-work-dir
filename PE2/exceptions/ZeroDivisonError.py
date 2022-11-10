# value = 1
# value /= 0

# Note:

# ZeroDivisionError is a special case of more a general exception class named ArithmeticError;
# ArithmeticError is a special case of a more general exception class named just Exception;
# Exception is a special case of a more general class named BaseException;
# We can describe it in the following way (note the direction of the arrows - they always point to the more general entity):

# BaseException
# ↑
# Exception
# ↑
# ArithmeticError
# ↑
# ZeroDivisionError


# We're going to show you how this generalization works. Let's start with some really simple code.

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Oooppsss...")

print("THE END.")

# Something has changed in it - we've replaced ZeroDivisionError with ArithmeticError.
# Thus, the code's output remains unchanged.
# This also means that replacing the exception's name with
# either Exception or BaseException won't change the program's behavior.

try:
    y = 1 / 0
except ArithmeticError:
    print("Oooppsss...")

print("THE END.")

# Let's summarize:

# each exception raised falls into the first matching branch;
# the matching branch doesn't have to specify the same exception exactly 
# - it's enough that the exception is more general (more abstract) than the raised one.

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")

# Will it change anything if we swap the two except branches around? Just like here below:

try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")

print("THE END.")

# Why, if the exception raised is the same as previously?

# The exception is the same, but the more general exception is now listed first - it will catch all zero divisions too. 
# It also means that there's no chance that any exception hits the ZeroDivisionError branch. 
# This branch is now completely unreachable.

# Remember:

# the order of the branches matters!
# don't put more general exceptions before more concrete ones;
# this will make the latter one unreachable and useless;
# moreover, it will make your code messy and inconsistent;
# Python won't generate any error messages regarding this issue.
