# The itermonthdates() method

# The Calendar class has several methods that return an iterator. 
# One of them is the itermonthdates method, which requires specifying the year and month.

# As a result, all days in the specified month and year are returned, 
# as well as all days before the beginning of the month or the end of the month that are necessary 
# to get a complete week.

# Each day is represented by a datetime.date object. Take a look at the example in the editor.

import calendar  

c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")


# The code displays all days in November 2019. Because the first day of November 2019 was a Friday, 
# the following days are also returned to get the complete week: 
# 10/28/2019 (Monday) 10/29/2019 (Tuesday) 10/30/2019 (Wednesday) 10/31/2019 (Thursday).

# The last day of November 2019 was a Saturday, 
# so in order to keep the complete week, one more day is returned 12/01/2019 (Friday).

