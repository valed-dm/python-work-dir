# The two-parameter replace() method returns a copy of the original string 
# in which all occurrences of the first argument have been replaced by the second argument.

# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("[Apple juice]".replace("juice", ""))
print()

print("[Apple juice]".replace("", "*"))
print("[Apple juice]".replace(" ", "*"))
print()

# The three-parameter replace() variant uses the third argument (a number) to limit the number of replacements.
# Look at the modified example code below:

print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))