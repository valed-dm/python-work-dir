# Processing text files: continued
# Reading a text file's contents can be performed using several different methods - 
# none of them is any better or worse than any other. It's up to you which of them you prefer and like.

# Some of them will sometimes be handier, and sometimes more troublesome. 
# Be flexible. Don't be afraid to change your preferences.

# The most basic of these methods is the one offered by the read() function, 
# which you were able to see in action in the previous lesson.

# If applied to a text file, the function is able to:

# read a desired number of characters (including just one) from the file, and return them as a string;
# read all the file contents, and return them as a string;
# if there is nothing more to read (the virtual reading head reaches the end of the file), 
# the function returns an empty string.

# We'll start with the simplest variant and use a file named text.txt. 
# The file has the following contents:

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# text.txt


# Now look at the code in the editor, and let's analyze it.

from os import strerror

try:
    cnt = 0
    print_interval = 1 # for every character = 1
    s = open('/Users/dmitrijvaledinskij/Python/data/zen_of_python.txt', "rt")
    print('\n', s, '\n')
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        # if cnt % print_interval == 0:
        #     print(ch, end='')
        # else:
        #     print('', end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

# The routine is rather simple:

# use the try-except mechanism and open the file of the predetermined name (text.txt in our case)
# try to read the very first character from the file (ch = s.read(1))
# if you succeed (this is proven by a positive result of the while condition check), 
# output the character (note the end= argument - it's important! 
# You don't want to skip to a new line after every character!);
# update the counter (cnt), too;
# try to read the next character, and the process repeats.
