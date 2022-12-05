# Diagnosing stream problems: continued
# If you are a very careful programmer, you may feel the need to use the sequence 
# of statements similar to those presented in the editor.

import errno

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)


# Fortunately, there is a function that can dramatically simplify the error handling code.

# Its name is strerror(), and it comes from the os module and expects just one argument - an error number.

# Its role is simple: you give an error number and get a string describing the meaning of the error.

# Note: if you pass a non-existent error code (a number which is not bound to any actual error), 
# the function will raise ValueError exception.

# Now we can simplify our code in the following way:

from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))


# Okay. Now it's time to deal with text files and get familiar with some basic techniques 
# you can use to process them.