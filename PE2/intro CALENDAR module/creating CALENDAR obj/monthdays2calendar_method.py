# The monthdays2calendar() method
# The Calendar class has several other useful methods that you can learn more about 
# in the documentation (https://docs.python.org/3/library/calendar.html).

# One of them is the monthdays2calendar method, which takes 
# the year and month, and then returns a list of weeks in a specific month. 
# Each week is a tuple consisting of day numbers and weekday numbers. 
# Look at the code in the editor.

import calendar  

c = calendar.Calendar()

for data in c.monthdays2calendar(2020, 12):
    print(data)


# Note that the days numbers outside the month are represented by 0, 
# while the weekday numbers are a number from 0-6, where 0 is Monday and 6 is Sunday.

# In a moment, this method may be useful for you to complete a laboratory task. 
# Are you ready?

