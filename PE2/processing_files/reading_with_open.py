# Processing text files: continued
# The last example we want to present shows a very interesting trait of the object returned by the open() function in text mode.

# We think it may surprise you - the object is an instance of the iterable class.

# Strange? Not at all. Usable? Yes, absolutely.

# The iteration protocol defined for the file object is very simple - its __next__ method just returns the next line read in from the file.

# Moreover, you can expect that the object automatically invokes close() when any of the file reads reaches the end of the file.

# Look at the editor and see how simple and clear the code has now become.

from os import strerror

try:
    ccnt = lcnt = 0
    for line in open('/Users/dmitrijvaledinskij/Python/data/zen_of_python.txt', 'rt'):
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
