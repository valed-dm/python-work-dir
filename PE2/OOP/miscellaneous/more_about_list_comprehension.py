# You should be able to remember the rules governing the creation and use of a very special Python phenomenon named list comprehension - a simple and very impressive way of creating lists and their contents.

# In case you need it, we've provided a quick reminder in the editor.

# There are two parts inside the code, both creating a list containing a few of the first natural powers of ten.

# The former uses a routine way of utilizing the for loop, while the latter makes use of the list comprehension and builds the list in situ, without needing a loop, or any other extended code.

# It looks like the list is created inside itself - it's not true, of course, as Python has to perform nearly the same operations as in the first snippet, but it is indisputable that the second formalism is simply more elegant, and lets the reader avoid any unnecessary details.

# The example outputs two identical lines containing the following text:

# [1, 10, 100, 1000, 10000, 100000]
# [1, 10, 100, 1000, 10000, 100000]

# Run the code to check if we're right.

list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

print(list_1)
print(list_2)
