# Date and time operations
# Sooner or later you'll have to perform some calculations on the date and time. 
# Fortunately, there's a class called timedelta in the datetime module that was created for just such a purpose.

# To create a timedelta object, just do subtraction on the date or datetime objects, 
# just like we did in the example in the editor. Run it.

from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)

# Result:

# 366 days, 0:00:00
# 365 days, 9:07:00
# output

# The example shows subtraction for both the date and datetime objects.

# In the first case, we receive the difference in days, which is 366 days. 
# Note that the difference in hours, minutes, and seconds is also displayed.

# In the second case, we receive a different result, 
# because we specified the time that was included in the calculations.
# As a result, we receive 365 days, 9 hours, and 7 minutes.

# In a moment you'll learn more about creating timedelta objects and about the operations you can do with them.

