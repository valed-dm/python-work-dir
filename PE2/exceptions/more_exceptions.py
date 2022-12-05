# More about exceptions
# Discussing object programming offers a very good opportunity to return to exceptions. The objective nature of Python's exceptions makes them a very flexible tool, able to fit to specific needs, even those you don't yet know about.

# Before we dive into the objective face of exceptions, we want to show you some syntactical and semantic aspects of the way in which Python treats the try-except block, as it offers a little more than what we have presented so far.

# The first feature we want discuss here is an additional, possible branch that can be placed inside (or rather, directly behind) the try-except block - it's the part of the code starting with else - just like in the example in the editor.


# A code labelled in this way is executed when (and only when) no exception has been raised inside the try: part. We can say that exactly one branch can be executed after try: - either the one beginning with except (don't forget that there can be more than one branch of this kind) or the one starting with else.

# Note: the else: branch has to be located after the last except branch.

# The example code produces the following output:

# Everything went fine
# 0.5
# Division failed
# None

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else:
        print("Everything went fine")
        return n


print(reciprocal(2))
print(reciprocal(0))

# The try-except block can be extended in one more way - by adding a part headed by the finally keyword (it must be the last branch of the code designed to handle exceptions).

# Note: these two variants (else and finally) aren't dependent in any way, and they can coexist or occur independently.

# The finally block is always executed (it finalizes the try-except block execution, hence its name), no matter what happened earlier, even when raising an exception, no matter whether this has been handled or not.

# Look at the code in the editor. It outputs:

# Everything went fine
# It's time to say good bye
# 0.5
# Division failed
# It's time to say good bye
# None


def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n


print(reciprocal(2))
print(reciprocal(0))
