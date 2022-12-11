# Key takeaways

# 1. In the calendar module, the days of the week are displayed from Monday to Sunday.
# Each day of the week has its representation in the form of an integer,
# where the first day of the week (Monday) is represented by the value 0,
# while the last day of the week (Sunday) is represented by the value 6.


# 2. To display a calendar for any year, call the calendar function with the year passed as its argument, e.g.:

import calendar
# print(calendar.calendar(2020))
calendar.prcal(2022)

print('-------------------')


# Note: A good alternative to the above function is the function called prcal,
#  which also takes the same parameters as the calendar function,
# but doesn't require the use of the print function to display the calendar.


# 3. To display a calendar for any month of the year, call the month function,
# passing year and month to it.
# For example:

# print(calendar.month(2020, 9))
calendar.prmonth(2022, 9)

print('-------------------')
# Note: You can also use the prmonth function, which has the same parameters as the month function,
# but doesn't require the use of the print function to display the calendar.


# 4. The setfirstweekday function allows you to change the first day of the week.
# It takes a value from 0 to 6, where 0 is Sunday and 6 is Saturday.


# 5. The result of the weekday function is a day of the week as an integer value for a given year, month, and day:

print(calendar.weekday(2020, 9, 29))  # This displays 1, which means Tuesday.

print('-------------------')

# 6. The weekheader function returns the weekday names in a shortened form.
# The weekheader method requires you to specify the width in characters for one day of the week.
# If the width you provide is greater than 3, you'll still get the abbreviated weekday names
# consisting of only three characters.
# For example:

print(calendar.weekheader(2))  # This display: Mo Tu We Th Fr Sa Su

print('-------------------')

# 7. A very useful function available in the calendar module is the function called isleap,
# which, as the name suggests, allows you to check whether the year is a leap year or not:

print(calendar.isleap(2020))  # This displays: True

print('-------------------')

# 8. You can create a calendar object yourself using the Calendar class,
# which, when creating its object,
# allows you to change the first day of the week with the optional firstweekday parameter, e.g.:


c = calendar.Calendar(2)

for weekday in c.iterweekdays():
    print(weekday, end=" ")


# Result: 2 3 4 5 6 0 1


# The iterweekdays returns an iterator for weekday numbers.
# The first value returned is always equal to the value of the firstweekday property.

# Exercise 1

# What is the output of the following snippet?
print('\n----------------')


import calendar

print(calendar.weekheader(1))
print(calendar.weekheader(2))
print(calendar.weekheader(3))

print('\n----------------')

c = calendar.Calendar()

for weekday in c.iterweekdays():
    print(weekday, end=" ")
