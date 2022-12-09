# Date and time formatting (part 1)

# All datetime module classes presented so far have a method called strftime. 
# This is a very important method, because it allows us to return the date and time in the format we specify.

# The strftime method takes only one argument in the form of a string specifying the format 
# that can consist of directives.

# A directive is a string consisting of the character % (percent) and a lowercase or uppercase letter, 
# e.g., the directive %Y means the year with the century as a decimal number. 
# Let's see it in an example. Run the code in the editor.

# Result:

# 2020/01/04
# output

# In the example, we passed a format consisting of three directives separated by / (slash) to the strftime method. 
# Of course, the separator character can be replaced by another character, or even by a string.

# You can put any characters in the format, but only recognizable directives will be replaced with 
# the appropriate values. In our format we've used the following directives:

# %Y – returns the year with the century as a decimal number. In our example, this is 2020.
# %m – returns the month as a zero-padded decimal number. In our example, it's 01.
# %d – returns the day as a zero-padded decimal number. In our example, it's 04.
# Note: You can find all available directives here:
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes


from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))
print(d.strftime('%d/%m/%Y'))
print('----------------')
print(d.strftime('%y/%m/%d'))
print(d.strftime('%dd/%mm/%yy'))
