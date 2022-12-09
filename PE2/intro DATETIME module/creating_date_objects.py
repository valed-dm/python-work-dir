# Getting the current local date and creating date objects
# One of the classes provided by the datetime module is a class called date. Objects of this class represent a date consisting of the year, month, and day. Look at the code in the editor to see what it looks like in practice and get the current local date using the today method.

# Run the code to see what happens.

# The today method returns a date object representing the current local date. Note that the date object has three attributes: year, month, and day.

# Be careful, because these attributes are read-only. To create a date object, you must pass the year, month, and day parameters as follows:

from datetime import date

my_date = date(2019, 11, 4)
print(my_date)

print('-----------------')

# Run the example to see what happens.

# When creating a date object, keep the following restrictions in mind:

# Parameter	Restrictions
# year	
# The year parameter must be greater than or equal to 1 (MINYEAR constant) and less than or equal to 9999 (MAXYEAR constant).

# month	
# The month parameter must be greater than or equal to 1 and less than or equal to 12.

# day	
# The day parameter must be greater than or equal to 1 and less than or equal to the last day of the given month and year.

# Note: Later in this course you'll learn how to change the default date format.


from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

print('-----------------')
for name in dir(date):
    print(name, end="\t")
print('----------------')
