# What day of the week is it?

# One of the more helpful methods that makes working with dates easier is the method called weekday. 
# It returns the day of the week as an integer,

# where 0 is Monday and 6 is Sunday.

# Run the code in the editor.

from datetime import date

d = date(2019, 11, 4)
print(d.weekday())

# Result:

# 0
# output


# The date class has a similar method called isoweekday, which also returns the day of the week as an integer, 
# but 1 is Monday, and 7 is Sunday:

from datetime import date

d = date(2019, 11, 4)
print(d.isoweekday())


# Result:

# 1
# output

# As you can see, for the same date we get a different integer, 
# but expressing the same day of the week. 
# The integer returned by the isodayweek method follows the ISO 85601 specification.

