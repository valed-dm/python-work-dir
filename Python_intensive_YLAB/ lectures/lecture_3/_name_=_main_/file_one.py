# Python if __name__ == __main__ Explained with Code Examples
# https://www.freecodecamp.org/news/if-name-main-python-example/


# When a Python interpreter reads a Python file, it first sets a few special variables.
# Then it executes the code from the file.

# One of those variables is called __name__.

# If you follow this article step-by-step and read its code snippets,
# you will learn how to use if __name__ == "__main__", and why it's so important.


# Python Modules Explained

# Python files are called modules and they are identified by the .py file extension.
# A module can define functions, classes, and variables.

# So when the interpreter runs a module, the __name__ variable will be set as  __main__
# if the module that is being run is the main program.

# But if the code is importing the module from another module, then the __name__  variable
# will be set to that module’s name.

# Let's take a look at an example.
# Create a Python module named file_one.py and paste this top level code inside:

# Python file one module
import file_two
from file_two import function_four


print("File one __name__ is set to: {}" .format(__name__))

# Now add another file named file_two.py and paste this code inside:

# Also, modify the code in file_one.py like this so we import the file_two module:
# Python module to execute


print("File one __name__ is set to: {}" .format(__name__))

# The result should look like this:
# File two __name__ is set to: file_two
# File one __name__ is set to: __main__

# But run file_two directly and you will see that its name is set to __main__:
# File two __name__ is set to: __main__

# The variable __name__ for the file/module that is run will be always __main__.
# But the __name__ variable for all other modules that are being imported will be set to their
# module's name.


# Python File Naming Conventions

# The usual way of using __name__ and __main__ looks like this:

# if __name__ == "__main__":
#    Do something here

# Let's see how this works in real life, and how to actually use these variables.

# Python module to execute


print("File one __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
    print("File one executed when ran directly")
else:
    print("File one executed when imported")

print("-------------------------------")

print("File one __name__ is set to: {}" .format(__name__))


def function_one():
    print("Function one is executed")


def function_two():
    print("Function two is executed")


if __name__ == "__main__":
    print("File one executed when ran directly")
else:
    print("File one executed when imported")


print("-------------------------------")

# Now the functions are loaded but not run.

# To run one of these functions modify the if __name__ == "__main__" part of file_one to look like this:

if __name__ == "__main__":
    print("File one executed when ran directly")
    function_two()
else:
    print("File one executed when imported")

# Also, you can run functions from imported files.
# To do that, modify the if __name__ == “__main__” part of file_one to look like this:

print("-------------------------------")

if __name__ == "__main__":
    print("File one executed when ran directly")
    function_two()
    file_two.function_three()
    function_four()
else:
    print("File one executed when imported")


# Conclusion

# There is a really nice use case for the __name__ variable, 
# whether you want a file that can be run as the main program or imported by other modules. 
# We can use an if __name__ == "__main__" block to allow or prevent parts of code from being run 
# when the modules are imported.

# When the Python interpreter reads a file, the __name__ variable is set as __main__ 
# if the module being run, or as the module's name if it is imported. 
# Reading the file executes all top level code, but not functions and classes 
# (since they will only get imported).

# Bra gjort! (That means "Well done" in Swedish!)