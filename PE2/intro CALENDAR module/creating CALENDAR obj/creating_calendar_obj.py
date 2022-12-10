# Creating a Calendar object

# The Calendar class constructor takes one optional parameter named firstweekday, by default equal to 0 (Monday).

# The firstweekday parameter must be an integer between 0-6. For this purpose, 
# we can use the already-known constants - look at the code in the editor.

import calendar  

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")


# The program will output the following result:

# 6 0 1 2 3 4 5
# output

# The code example uses the Calendar class method named iterweekdays, which returns an iterator for week day numbers.

# The first value returned is always equal to the value of the firstweekday property. 
# Because in our example the first value returned is 6, it means that the week starts on a Sunday.

