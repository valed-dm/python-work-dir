# Methods that return the current date and time
# The datetime class has several methods that return the current date and time. These methods are:

# today() — returns the current local date and time with the tzinfo attribute set to None;

# now() — returns the current local date and time the same as the today method, 
# unless we pass the optional argument tz to it. 
# The argument of this method must be an object of the tzinfo subclass;

# utcnow() — returns the current UTC date and time with the tzinfo attribute set to None.
# Run the code in the editor to see them all in practice. What can you say about the output?

# As you can see, the result of all the three methods is the same.
# The small differences are caused by the time elapsed between subsequent calls.

# Note: You can read more about tzinfo objects in the documentation.


from datetime import datetime

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())
