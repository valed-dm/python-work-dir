# 1. An exception is an event in a program execution's life caused by an abnormal situation. 
# The exception should he handled to avoid program termination. 
# The part of your code that is suspected of being the source of the exception should be put inside the try branch.

# When the exception happens, the execution of the code is not terminated, but instead jumps into the except branch. 
# This is the place where the handling of the exception should take place. 
# The general scheme for such a construction looks as follows:

# :
# # The code that always runs smoothly.
# :
# try:
#     :
#     # Risky code.
#     :
# except:
#     :
#     # Crisis management takes place here.
#     : 
# :
# # Back to normal.
# :


# 2. If you need to handle more than one exception coming from the same try branch, 
# you can add more than one except branch, but you have to label them with different exception names, 
# like this:

# :
# # The code that always runs smoothly.
# :
# try:
#     :
#     # Risky code.
#     :
# except Except_1:
#     # Crisis management takes place here.
# except Except_2:
#     # We save the world here.
# :
# # Back to normal.
# :


# At most, one of the except branches is executed 
# – none of the branches is performed when the raised exception doesn't match to the specified exceptions.


# 3. You cannot add more than one anonymous (unnamed) except branch after the named ones.

# :
# # The code that always runs smoothly.
# :
# try:
#     :
#     # Risky code.
#     :
# except Except_1:
#     # Crisis management takes place here.
# except Except_2:
#     # We save the world here.
# except:
#     # All other issues fall here.
# :
# # Back to normal.
# :

try:
    print("Let's try to do this")
    print("#"[2])
    print("We succeeded!")
except:
    print("We failed")
print("We're done")

try:
    print("alpha"[1/0])
except ZeroDivisionError:
    print("zero")
except IndexError:
    print("index")
except:
    print("some")

# 1. You cannot add more than one anonymous (unnamed) except branch after the named ones.

# :
# # The code that always runs smoothly.
# :
# try:
#     :
#     # Risky code.
#     :
# except Except_1:
#     # Crisis management takes place here.
# except Except_2:
#     # We save the world here.
# except:
#     # All other issues fall here.
# :
# # Back to normal.
# :


# 2. All the predefined Python exceptions form a hierarchy, i.e. some of them are more general (the one named BaseException is the most general one) while others are more or less concrete (e.g. IndexError is more concrete than LookupError).

# You shouldn't put more concrete exceptions before the more general ones inside the same except branche sequence. For example, you can do this:

# try:
#     # Risky code.
# except IndexError:
#     # Taking care of mistreated lists
# except LookupError:
#     # Dealing with other erroneous lookups


# but don't do that (unless you're absolutely sure that you want some part of your code to be useless)

# try:
#     # Risky code.
# except LookupError:
#     # Dealing with erroneous lookups
# except IndexError:
#     # You'll never get here 


# 3. The Python statement raise ExceptionName can raise an exception on demand. The same statement, but lacking ExceptionName, can be used inside the try branch only, and raises the same exception which is currently being handled.


# 4. The Python statement assert expression evaluates the expression and raises the AssertError exception when the expression is equal to zero, an empty string, or None. You can use it to protect some critical parts of your code from devastating data.