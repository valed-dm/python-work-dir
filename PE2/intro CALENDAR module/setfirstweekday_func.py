# The setfirstweekday() function
# As you already know, by default in the calendar module, the first day of the week is Monday. 
# However, you can change this behavior using a function called setfirstweekday.

# Do you remember the table showing the days of the week and their representation in the form of integer values? 
# It's time to use it, because the setfirstweekday method requires a parameter expressing the day of the week 
# in the form of an integer value. Take a look at the example in the editor.

import calendar

calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2020, 12)


# The example uses the calendar.SUNDAY constant, which contains a value of 6. Of course, 
# you could pass this value directly to the setfirstweekday function, but the version with a constant is more elegant.

# As a result, we get a calendar showing the month of December 2020, in which the first day of all the weeks is Sunday.