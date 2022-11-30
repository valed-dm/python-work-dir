# __module__ is a string, too - it stores the name of the module which contains the definition of the class.

# Let's check it - run the code in the editor.

# The code outputs:

# __main__
# __main__
# output

# As you know, any module named __main__ is actually not a module, but the file currently being run.

class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)
