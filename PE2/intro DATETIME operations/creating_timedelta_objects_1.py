# Creating timedelta objects: continued
# You already know how the timedelta object stores the passed arguments internally. 
# It's time to see how it can be used in practice.

# Let's look at some operations supported by the datetime module classes. 
# Run the code we've provided in the editor.

from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=2)
print('initial timedelta: -->', delta)

delta2 = delta * 2
print('timedelta multiplied by integer: -->', delta2)

d = date(2019, 10, 4) + delta2
print('timedelta added to date: -->', d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print('timedelta added to datetime: -->', dt)


# Result:

# 16 days, 2:00:00
# 32 days, 4:00:00
# 2019-11-05
# 2019-11-05 18:53:00
# output

# The timedelta object can be multiplied by an integer. 
# In our example, we multiply the object representing 16 days and 2 hours by 2.
# As a result, we receive a timedelta object representing 32 days and 4 hours.

# Note that both days and hours have been multiplied by 2. 
# Another interesting operation using the timedelta object is adding. 
# In the example, we've added the timedelta object to the date and datetime objects.

# As a result of these operations, we receive date and datetime objects 
# increased by days and hours stored in the timedelta object.

# The presented multiplication operation allows you to quickly increase the value of the timedelta object, while multiplication can also help you get a date from the future.

# Of course, the timedelta, date, and datetime classes support many more operations. 
# We encourage you to familiarize yourself with them in the documentation.



