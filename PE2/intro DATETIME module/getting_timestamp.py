# Getting a timestamp
# There are many converters available on the Internet that can calculate a timestamp 
# based on a given date and time, but how can we do it in the datetime module?

# This is possible thanks to the timestamp method provided by the datetime class. 
# Look at the code in the editor.

from datetime import datetime

dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())

# Result:

# Timestamp: 1601823300.0
# output

# The timestamp method returns a float value expressing the number of seconds elapsed 
# between the date and time indicated by the datetime object and January 1, 1970, 00:00:00 (UTC).