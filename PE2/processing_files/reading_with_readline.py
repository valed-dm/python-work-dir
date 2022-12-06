# Processing text files: readline()
# If you want to treat the file's contents as a set of lines, not a bunch of characters,
# the readline() method will help you with that.

# The method tries to read a complete line of text from the file,
# and returns it as a string in the case of success. Otherwise, it returns an empty string.

# This opens up new opportunities - now you can also count lines easily, not only characters.

# Let's make use of it. Look at the code in the editor.

# As you can see, the general idea is exactly the same as in both previous examples.

from os import strerror

try:
    ccnt = lcnt = 0
    s = open('/Users/dmitrijvaledinskij/Python/data/zen_of_python.txt', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
