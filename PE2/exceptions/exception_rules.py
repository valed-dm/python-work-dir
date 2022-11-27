# Don't forget that:

# the except branches are searched in the same order in which they appear in the code;
# you must not use more than one except branch with a certain exception name;
# the number of different except branches is arbitrary 
# - the only condition is that if you use try, you must put at least one except (named or not) after it;
# the except keyword must not be used without a preceding try;
# if any of the except branches is executed, no other branches will be visited;
# if none of the specified except branches matches the raised exception, 
# the exception remains unhandled (we'll discuss it soon)
# if an unnamed except branch exists (one without an exception name), it has to be specified as the last.
# try:
#     :
# except exc1:
#     :
# except exc2:
#     :
# except:
#     :

# We've modified the previous program - we've removed the ZeroDivisionError branch.

# What happens now if the user enters 0 as an input?

# As there are no dedicated branches for division by zero, the raised exception falls into the general (unnamed) branch; this means that in this case, the program will say:

# Oh dear, something went wrong...
# THE END.

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")

# Let's spoil the code once again.

# Look at the program in the editor. This time, we've removed the unnamed branch.

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")

print("THE END.")

# The user enters 0 once again and:

# the exception raised won't be handled by ValueError - it has nothing to do with it;
# as there's no other branch, you should to see this message:

# Traceback (most recent call last):
# File "exc.py", line 3, in 
# y = 1 / x
# ZeroDivisionError: division by zero
# output


# You've learned a lot about exception handling in Python. In the next section, we will focus on Python built-in exceptions and their hierarchies.

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")