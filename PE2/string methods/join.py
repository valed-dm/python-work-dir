# The join() method is rather complicated, so let us guide you step by step through it:

# as its name suggests, the method performs a join - it expects one argument as a list; it must be assured that all the list's elements are strings - the method will raise a TypeError exception otherwise;
# all the list's elements will be joined into one string but...
# ...the string from which the method has been invoked is used as a separator, put among the strings;
# the newly created string is returned as a result.
# Take a look at the example in the editor. Let's analyze it:

# the join() method is invoked from within a string containing a comma (the string can be arbitrarily long, or it can be empty)
# the join's argument is a list containing three strings;
# the method returns a new string.
# Here it is:

# Demonstrating the join() method:
print(" - ".join(["omicron", "pi", "rho"]))
