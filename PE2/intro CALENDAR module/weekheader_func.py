# The weekheader() function
# You've probably noticed that the calendar contains weekly headers in a shortened form. 
# If needed, you can get short weekday names using the weekheader method.

# The weekheader method requires you to specify the width in characters for one day of the week. 
# If the width you provide is greater than 3, you'll still get the abbreviated weekday names 
# consisting of three characters.

# So let's look at how to get a smaller header. 
# Run the code in the editor.

import calendar


print(calendar.weekheader(2))
print(calendar.weekheader(3))

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.weekheader(4))


# Result:

# Mo Tu We Th Fr Sa Su
# output

# Note: If you change the first day of the week, e.g., using the setfirstweekday function, 
# it'll affect the result of the weekheader function.

