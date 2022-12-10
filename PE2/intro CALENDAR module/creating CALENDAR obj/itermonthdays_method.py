# Other methods that return iterators
# Another useful method in the Calendar class is the method called itermonthdays, 
# which takes year and month as parameters, and then returns the iterator to the days of the week represented by numbers.

# Take a look at the example in the editor.

import calendar  

c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")


# You’ll have certainly noticed the large number of 0s returned as a result of the example code. 
# These are days outside the specified month range that are added to keep the complete week.

# The first four zeros represent 10/28/2019 (Monday) 10/29/2019 (Tuesday) 10/30/2019 (Wednesday) 10/31/2019 (Thursday). 
# The remaining numbers are days in the month, except the last value of 0, which replaces the date 12/01/2019 (Sunday).

# There are four other similar methods in the Calendar class that differ in data returned:

# itermonthdays2 – returns days in the form of tuples 
# consisting of a day of the month number and a week day number;
print('\n----------------')

for iter in c.itermonthdays2(2019, 11):
    print(iter, end=" ")

# itermonthdays3 – returns days in the form of tuples 
# consisting of a year, a month, and a day of the month numbers. 
# This method has been available since version 3.7;
print('\n----------------')

for iter in c.itermonthdays3(2019, 11):
    print(iter, end=" ")

# itermonthdays4 – returns days in the form of tuples 
# consisting of a year, a month, a day of the month, and a day of the week numbers. 
# This method has been available since Python version 3.7.
print('\n----------------')

for iter in c.itermonthdays4(2019, 11):
    print(iter, end=" ")

# For testing purposes, use the example above and see how the return values of the described methods look in practice.