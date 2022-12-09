# Creating a date object using the ISO format
# The datetime module provides several methods to create a date object. 
# One of them is the fromisoformat method, which takes a date in the YYYY-MM-DD format 
# compliant with the ISO 8601 standard.

# The ISO 8601 standard defines how the date and time are represented. 
# It's often used, so it's worth taking a moment to familiarize yourself with it. 
# Take a look at the picture describing the values required by the format:


# The ISO 8601 date and time format
# YYYY-MM-DD


# Now look at the code in the editor and run it.

# In our example, YYYY is 2019, MM is 11 (November), and DD is 04 (fourth day of November).

# When substituting the date, be sure to add 0 before a month or a day that is expressed by a number less than 10.

# Note: The fromisoformat method has been available in Python since version 3.7.


from datetime import date

d = date.fromisoformat('2019-11-04')
print(d)
