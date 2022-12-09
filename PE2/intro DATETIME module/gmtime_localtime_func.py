# The gmtime() and localtime() functions
# Some of the functions available in the time module require knowledge of the struct_time class, 
# but before we get to know them, let's see what the class looks like:

# time.struct_time:
#     tm_year   # specifies the year
#     tm_mon    # specifies the month (value from 1 to 12)
#     tm_mday   # specifies the day of the month (value from 1 to 31)
#     tm_hour   # specifies the hour (value from 0 to 23)
#     tm_min    # specifies the minute (value from 0 to 59)
#     tm_sec    # specifies the second (value from 0 to 61 )
#     tm_wday   # specifies the weekday (value from 0 to 6)
#     tm_yday   # specifies the year day (value from 1 to 366)
#     tm_isdst  # specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
#     tm_zone   # specifies the timezone name (value in an abbreviated form)
#     tm_gmtoff # specifies the offset east of UTC (value in seconds)


# The struct_time class also allows access to values using indexes. Index 0 returns the value in tm_year, 
# while 8 returns the value in tm_isdst.

# The exceptions are tm_zone and tm_gmoff, which cannot be accessed using indexes. 
# Let's look at how to use the struct_time class in practice. Run the code in the editor.

# Result:

# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
# output

# The example shows two functions that convert the elapsed time from the Unix epoch to the struct_time object. 
# The difference between them is that the gmtime function returns the struct_time object in UTC, 
# while the localtime function returns local time. For the gmtime function, the tm_isdst attribute is always 0.


import time

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))
