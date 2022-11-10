def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")

# The raise instruction raises the specified exception named exc 
# as if it was raised in a normal (natural) way:

# raise exc


# Note: raise is a keyword.

# The instruction enables you to:

# simulate raising actual exceptions (e.g., to test your handling strategy)
# partially handle an exception and make another part of the code responsible 
# for completing the handling (separation of concerns).

# In this way, you can test your exception handling routine without forcing the code to do stupid things.

def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise

try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")

# The raise instruction may also be utilized in the following way (note the absence of the exception's name):

# raise


# There is one serious restriction: this kind of raise instruction may be used inside the except branch only; using it in any other context causes an error.

# The instruction will immediately re-raise the same exception as currently handled.


# Thanks to this, you can distribute the exception handling among different parts of the code.

# Look at the code in the editor. Run it - we'll see it in action.

# The ZeroDivisionError is raised twice:

# first, inside the try part of the code (this is caused by actual zero division)
# second, inside the except part by the raise instruction.
# In effect, the code outputs:

# I did it again!
# I see!
# THE END.