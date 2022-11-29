# The try-except instruction gives you the chance to avoid issues with non-existent properties.

# It's easy - look at the code in the editor.

# As you can see, this action isn't very sophisticated. Essentially, we've just swept the issue under the carpet.

# Fortunately, there is one more way to cope with the issue.


# Python provides a function which is able to safely check if any object/class contains a specified property. The function is named hasattr, and expects two arguments to be passed to it:

# the class or the object being checked;
# the name of the property whose existence has to be reported (note: it has to be a string containing the attribute name, not the name alone)
# The function returns True or False.

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

# try:
#     print(example_object.b)
# except AttributeError:
#     pass

if hasattr(example_object, 'b'):
    print(example_object.b)
