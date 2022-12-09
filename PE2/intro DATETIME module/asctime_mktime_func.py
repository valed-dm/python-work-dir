# The asctime() and mktime() functions
# The time module has functions that expect a struct_time object or a tuple that stores values according 
# to the indexes presented when discussing the struct_time class. Run the example in the editor.

# Result:

# Mon Nov  4 14:53:00 2019
# 1572879180.0
# output

# The first of the functions, called asctime, converts a struct_time object or a tuple to a string. 
# Note that the familiar gmtime function is used to get the struct_time object. 
# If you don't provide an argument to the asctime function, 
# the time returned by the localtime function will be used.

# The second function called mktime converts a struct_time object or a tuple that expresses 
# the local time to the number of seconds since the Unix epoch. 
# In our example, we passed a tuple to it, which consists of the following values:

# 2019 => tm_year
# 11 => tm_mon
# 4 => tm_mday
# 14 => tm_hour
# 53 => tm_min
# 0 => tm_sec
# 0 => tm_wday
# 308 => tm_yday
# 0 => tm_isdst


import time

timestamp = 1572879180
st = time.gmtime(timestamp) # struct_time class

print(st)
print(st.tm_year)
print(st.tm_mon)
print(st.tm_yday)
print(st.tm_wday)
print(time.asctime(st))
print(time.asctime())
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))

