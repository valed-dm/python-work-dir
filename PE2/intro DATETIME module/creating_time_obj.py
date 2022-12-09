# Creating time objects
# You already know how to present a date using the date object. 
# The datetime module also has a class that allows you to present time. 
# Can you guess its name? Yes, it's called time:

# time(hour, minute, second, microsecond, tzinfo, fold)


# The time class constructor accepts the following optional parameters:

# Parameter	Restrictions
# hour
# The hour parameter must be greater than or equal to 0 and less than 23.

# minute
# The minute parameter must be greater than or equal to 0 and less than 59.

# second
# The second parameter must be greater than or equal to 0 and less than 59.

# microsecond
# The microsecond parameter must be greater than or equal to 0 and less than 1000000.

# tzinfo
# The tzinfo parameter must be a tzinfo subclass object or None (default).

# fold
# The fold parameter must be 0 or 1 (default 0).

# The tzinfo parameter is associated with time zones, while fold with wall times. 
# We won't use them during this course, but we encourage you to familiarize yourself with them.

# Let's look at how to create a time object in practice. Run the code in the editor.

# Result:

# Time: 14:53:20.000001
# Hour: 14
# Minute: 53
# Second: 20
# Microsecond: 1
# output

# In the example, we passed four parameters to the class constructor: 
# hour, minute, second, and microsecond. Each of them can be accessed using the class attributes.

# Note: Soon we'll tell you how you can change the default time formatting.


from datetime import time

t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)
