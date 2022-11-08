# 1. Strings can be compared to strings using general comparison operators, 
# but comparing them to numbers gives no reasonable result, 
# because no string can be equal to any number. For example:

# string == number is always False;
# string != number is always True;
# string >= number always raises an exception.

# 2. Sorting lists of strings can be done by:

# a function named sorted(), creating a new, sorted list;
# a method named sort(), which sorts the list in situ

# 3. A number can be converted to a string using the str() function.

# 4. A string can be converted to a number (although not every string) 
# using either the int() or float() function. The conversion fails if a string 
# doesn't contain a valid number image (an exception is raised then).

print('smith' > 'Smith')
print('Smiths' < 'Smith')
print('Smith' > '1000')
print('11' < '8')
print()

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])
print()

s1 = '12.8'
i = int(s1) # ValueError: invalid literal for int() with base 10: '12.8'
print(i)
s2 = str(i)
f = float(s2)
print(s1 == s2)
print(f)