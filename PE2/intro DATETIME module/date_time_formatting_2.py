# Date and time formatting (part 2)
# Time formatting works in the same way as date formatting, but requires the use of appropriate directives. Let's take a closer look at a few of them in the editor.

# Result:

# 14:53:00
# 20/November/04 14:53:00
# output

# The first of the formats used concerns only time. As you can guess, %H returns the hour as a zero-padded decimal number, %M returns the minute as a zero-padded decimal number, while %S returns the second as a zero-padded decimal number. In our example, %H is replaced by 14, %M by 53, and %S by 00.

# The second format used combines date and time directives. There are two new directives, %Y and %B. The directive %Y returns the year without a century as a zero-padded decimal number (in our example it's 20). The %B directive returns the month as the locale’s full name (in our example, it's November).

# In general, you've got a lot of freedom in creating formats, but you must remember to use the directives properly. As an exercise, you can check what happens if, for example, you try to use the %Y directive in the format passed to the time object's strftime method. Try to find out why you got this result yourself. Good luck!


from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))
print(t.strftime("%Y:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))
print(dt.strftime("%Y/%B/%d %H:%M:%S"))
