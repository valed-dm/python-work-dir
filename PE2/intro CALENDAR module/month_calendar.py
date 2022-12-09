# Calendar for a specific month
# The calendar module has a function called month, which allows you to display a calendar for a specific month.
# Its use is really simple, you just need to specify the year and month - check out the code in the editor.

# The example displays the calendar for November 2020. As in the calendar function, you can change
# the default formatting using the following parameters:

# w – date column width (default 2)
# l – number of lines per week (default 1)

# Note: You can also use the prmonth function, which has the same parameters as the month function,
# but doesn't require you to use the print function to display the calendar.


import calendar
print(calendar.month(2022, 11))


calendar.prmonth(2022, 12)
