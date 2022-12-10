# How do we check if a year is a leap year?

# The calendar module provides two useful functions to check whether years are leap years.


# February 29th


# The first one, called isleap, returns True if the passed year is leap, or False otherwise. 
# The second one, called leapdays, returns the number of leap years in the given range of years.

# Run the code in the editor.

import calendar

print(calendar.isleap(2017))
print(calendar.leapdays(2010, 2021))  # Up to but not including 2021.


# Result:

# True
# 3
# output

# In the example, we obtain the result 3, because in the period from 2010 to 2020 there are only three leap years (note: 2021 is not included). They are the years 2012, 2016, and 2020.

