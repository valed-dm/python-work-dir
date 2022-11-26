# The islower() method is a fussy variant of isalpha() - it accepts lower-case letters only.
# Example 1: Demonstrating the islower() method:
print("Moooo".islower())
print('moooo12345?'.islower())
print()

# The isspace() method identifies whitespaces only 
# - it disregards any other character (the result is False then).
# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())
print()

# The isupper() method is the upper-case version of islower() - it concentrates on upper-case letters only.
# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOOO1234567890?!#$'.isupper())