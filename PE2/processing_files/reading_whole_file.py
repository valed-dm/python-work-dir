# Processing text files: continued
# If you're absolutely sure that the file's length is safe and you can read the whole file 
# to the memory at once, you can do it - the read() function, 
# invoked without any arguments or with an argument that evaluates to None, will do the job for you.

# Remember - reading a terabyte-long file using this method may corrupt your OS.

# Don't expect miracles - computer memory isn't stretchable.

# Look at the code in the editor. What do you think of it?

# Let's analyze it:

# open the file as previously;
# read its contents by one read() function invocation;
# next, process the text, iterating through it with a regular for loop, 
# and updating the counter value at each turn of the loop;
# The result will be exactly the same as previously.

# import os
from os import strerror

try:
    cnt = 0
    s = open('/Users/dmitrijvaledinskij/Python/data/zen_of_python.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

# for name in dir(os):
#     print(name, end="\t")