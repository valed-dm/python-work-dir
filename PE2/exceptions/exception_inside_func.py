def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

bad_fun(0)

print("THE END.")

# It's also possible to let the exception propagate outside the function. Let's test it now.

def bad_fun(n):
    return 1 / n

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")

# The problem has to be solved by the invoker (or by the invoker's invoker, and so on).

# The program outputs:

# What happened? An exception was raised!
# THE END.
# output


# Note: the exception raised can cross function and module boundaries, and travel through the invocation chain looking for a matching except clause able to handle it.

# If there is no such clause, the exception remains unhandled, and Python solves the problem in its standard way - by terminating your code and emitting a diagnostic message.