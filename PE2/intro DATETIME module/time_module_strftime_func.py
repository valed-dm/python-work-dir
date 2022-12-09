# The strftime() function in the time module
# You probably won't be surprised to learn that the strftime function is available in the time module.
# It differs slightly from the strftime methods in the classes provided by the datetime module because,
# in addition to the format argument, it can also take (optionally) a tuple or struct_time object.

# If you don't pass a tuple or struct_time object, the formatting will be done using the current local time.
# Take a look at the example in the editor.

# Our result looks as follows:

# 2019/11/04 14:53:00
# 2020/10/12 12:19:40
# sample output

# Creating a format looks the same as for the strftime methods in the datetime module.
# In our example, we use the %Y, %m, %d, %H, %M, and %S directives that you already know.

# In the first function call, we format the struct_time object, while in the second call
# (without the optional argument), we format the local time.
# You can find all available directives in the time module here:
# https://docs.python.org/3/library/time.html#time.strftime


import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))
