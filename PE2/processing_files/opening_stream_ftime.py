# Opening the stream for the first time
# Imagine that we want to develop a program that reads content of the text file named: C:\Users\User\Desktop\file.txt.

# How to open that file for reading? Here's the relevant snippet of the code:

try:
    stream = open("C:\Users\User\Desktop\file.txt", "rt")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)


# What's going on here?

# we open the try-except block as we want to handle runtime errors softly;
# we use the open() function to try to open the specified file (note the way we've specified the file name)
# the open mode is defined as text to read (as text is the default setting, we can skip the t in mode string)
# in case of success we get an object from the open() function and we assign it to the stream variable;
# if open() fails, we handle the exception printing full error information (it's definitely good to know what exactly happened)
# Pre-opened streams
# We said earlier that any stream operation must be preceded by the open() function invocation. There are three well-defined exceptions to the rule.

# When our program starts, the three streams are already opened and don't require any extra preparations. What's more, your program can use these streams explicitly if you take care to import the sys module:

import sys


# because that's where the declaration of the three streams is placed.




# The names of these streams are: sys.stdin, sys.stdout, and sys.stderr.

# Let's analyze them:

sys.stdin
# stdin (as standard input)
# the stdin stream is normally associated with the keyboard, pre-open for reading and regarded as the primary data source for the running programs;
# the well-known input() function reads data from stdin by default.

sys.stdout
# stdout (as standard output)
# the stdout stream is normally associated with the screen, pre-open for writing, regarded as the primary target for outputting data by the running program;
# the well-known print() function outputs the data to the stdout stream.

sys.stderr
# stderr (as standard error output)
# the stderr stream is normally associated with the screen, pre-open for writing, regarded as the primary place where the running program should send information on the errors encountered during its work;
# we haven't presented any method to send the data to this stream (we will do it soon, we promise)
# the separation of stdout (useful results produced by the program) from the stderr (error messages, undeniably useful but does not provide results) gives the possibility of redirecting these two types of information to the different targets. More extensive discussion of this issue is beyond the scope of our course. The operation system handbook will provide more information on these issues.
