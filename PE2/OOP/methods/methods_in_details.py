# Let's summarize all the facts regarding the use of methods in Python classes.

# As you already know, a method is a function embedded inside a class.

# There is one fundamental requirement - a method is obliged to have at least one parameter (there are no such thing as parameterless methods - a method may be invoked without an argument, but not declared without parameters).

# The first (or only) parameter is usually named self. We suggest that you follow the convention - it's commonly used, and you'll cause a few surprises by using other names for it.

# The name self suggests the parameter's purpose - it identifies the object for which the method is invoked.

# If you're going to invoke a method, you mustn't pass the argument for the self parameter - Python will set it for you.

# The example in the editor shows the difference.

# The code outputs:

# method
# output

# Note the way we've created the object - we've treated the class name like a function, returning a newly instantiated object of the class.

# If you want the method to accept parameters other than self, you should:

# place them after self in the method's definition;
# deliver them during invocation without specifying self (as previously)
# Just like here:

class Classy:
    def method(self, par):
        print("method:", par)


obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)


# The code outputs:

# method: 1
# method: 2
# method: 3