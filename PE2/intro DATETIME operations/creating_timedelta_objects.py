# Creating timedelta objects
# You've already learned that a timedelta object can be returned as a result of subtracting 
# two date or datetime objects.

# Of course, you can also create an object yourself. 
# For this purpose, let's get acquainted with the arguments accepted by the class constructor, 
# which are: days, seconds, microseconds, milliseconds, minutes, hours, and weeks. 
# Each of them is optional and defaults to 0.

# The arguments should be integers or floating point numbers, 
# and can be either positive or negative. 
# Let's look at a simple example in the editor.

from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
delta_1 = timedelta(weeks=2.5, days=2.6, hours=3.7)
delta_2 = timedelta(weeks=1.725)
delta_3 = timedelta(weeks=-2)
print(delta)
print(delta_1)
print(delta_2)
print(delta_3)
print('----------------')
print(delta + delta_1 + delta_2 + delta_3)
print('----------------')

# Result:

# 16 days, 3:00:00
# output

# The result of 16 days is obtained by converting the weeks argument to days (2 weeks = 14 days) and adding the days argument (2 days). This is normal behavior, because the timedelta object only stores days, seconds, and microseconds internally. Similarly, the hour argument is converted to minutes. Take a look at the example below:

from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)


# Result:

# Days: 16
# Seconds: 10800
# Microseconds: 0
# output

# The result of 10800 is obtained by converting 3 hours into seconds. In this way the timedelta object stores the arguments passed during its creation. Weeks are converted to days, hours and minutes to seconds, and milliseconds to microseconds.