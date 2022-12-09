# The replace() method
# Sometimes you may need to replace the year, month, or day with a different value. 
# You can’t do this with the year, month, and day attributes because they're read-only. 
# In this case, you can use the method named replace.

# Run the code in the editor.

from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)


# Result:

# 1991-02-05
# 1992-01-16
# output

# The year, month, and day parameters are optional. 
# You can pass only one parameter to the replace method, e.g., year, or all three as in the example.

# The replace method returns a changed date object, so you must remember to assign it to some variable.

d = d.replace(year=2022)
print(d)