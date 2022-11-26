# The find() method is similar to index(), which you already know 
# - it looks for a substring and returns the index of first occurrence of this substring, but:

# it's safer - it doesn't generate an error for an argument containing a non-existent substring 
# (it returns -1 then)
# it works with strings only - don't try to apply it to any other sequence.

# Note: don't use find() if you only want to check if a single character occurs within a string
#  - the in operator will be significantly faster.

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

print("in usage:", "t" in t)

# If you want to perform the find, not from the string's beginning, 
# but from any position, you can use a two-parameter variant of the find() method. 
# Look at the example:

print('kappa'.find('a', 2))

# You can use the find() method to search for all the substring's occurrences, like here:

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop the publishing program PageMaker the (from Wikipedia) the"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)

# There is also a three-parameter mutation of the find() method 
# - the third argument points to the first index which won't be taken into consideration 
# during the search (it's actually the upper limit of the search).

# Look at our example below:

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))