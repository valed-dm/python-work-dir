# try:
#     x = int(input("Enter a number: "))
#     y = 1 / x
# except:
#     print("Oh dear, something went wrong...")

# print("THE END.i")


# This approach has one important disadvantage - if there is a possibility that more than one exception may skip into an except: branch, you may have trouble figuring out what actually happened.

# Just like in our code in the editor. Run it and see what happens.

# The message: Oh dear, something went wrong... appearing in the console says nothing about the reason, while there are two possible causes of the exception:

# non-integer data entered by the user;
# an integer value equal to 0 assigned to the x variable.

# Technically, there are two ways to solve the issue:

# build two consecutive try-except blocks, one for each possible exception reason (easy, but will cause unfavorable code growth)
# use a more advanced variant of the instruction.
# It looks like this:

# try:
#     :
# except exc1:
#     :
# except exc2:
#     :
# except:
#     :


# This is how it works:

# if the try branch raises the exc1 exception, it will be handled by the except exc1: block;
# similarly, if the try branch raises the exc2 exception, it will be handled by the except exc2: block;
# if the try branch raises any other exception, it will be handled by the unnamed except block.

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


# If you want to handle two or more exceptions in the same way, you can use the following syntax:

# try:
#     :
# except (exc1, exc2):
#     :


# You simply have to put all the engaged exception names into a comma-separated list and not to forget the parentheses.