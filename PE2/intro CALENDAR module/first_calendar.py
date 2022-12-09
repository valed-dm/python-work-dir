# Your first calendar
# You will start your adventure with the calendar module with a simple function called calendar, which allows you to display the calendar for the whole year. Let's look at how to use it to display the calendar for 2020. Run the code in the editor and see what happens.

# import calendar
# print(calendar.calendar(2022))

# The result displayed is similar to the result of the cal command available in Unix. If you want to change the default calendar formatting, you can use the following parameters:

# w – date column width (default 2)
# l – number of lines per week (default 1)
# c – number of spaces between month columns (default 6)
# m – number of columns (default 3)
# The calendar function requires you to specify the year, while the other parameters responsible for formatting are optional. We encourage you to try these parameters yourself.

# A good alternative to the above function is the function called prcal, which also takes the same parameters as the calendar function, but doesn't require the use of the print function to display the calendar. Its use looks like this:

import calendar
calendar.prcal(2022, m=5)
