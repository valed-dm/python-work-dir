# The split() method does what it says - it splits the string and builds a list of all detected substrings.
# The method assumes that the substrings are delimited by whitespaces 
# - the spaces don't take part in the operation, and aren't copied into the resulting list.

# Demonstrating the split() method:
str = "phi       chi\npsi".split()

print(str)

print(",".join(str))
print("\n".join(str))
print()

for i in str:
    print(i)