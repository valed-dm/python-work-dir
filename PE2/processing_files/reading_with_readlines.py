# Processing text files: readlines()
# Another method, which treats text file as a set of lines, not characters, is readlines().

# The readlines() method, when invoked without arguments, tries to read all the file contents, and returns a list of strings, one element per file line.

# If you're not sure if the file size is small enough and don't want to test the OS, you can convince the readlines() method to read not more than a specified number of bytes at once (the returning value remains the same - it's a list of a string).

# Feel free to experiment with the following example code to understand how the readlines() method works:

s = open('/Users/dmitrijvaledinskij/Python/data/zen_of_python.txt')
print(s.readlines())
# print(s.readlines(20))
# print(s.readlines(20))
# print(s.readlines(20))
s.close()

print()
# The maximum accepted input buffer size is passed to the method as its argument.

# You may expect that readlines() can process a file's contents more effectively than readline(), as it may need to be invoked fewer times.

# Note: when there is nothing to read from the file, the method returns an empty list. Use it to detect the end of the file.

# To the extent of the buffer's size, you can expect that increasing it may improve input performance, but there is no golden rule for it - try to find the optimal values yourself.


# Look at the code in the editor. We've modified it to show you how to use readlines().

# We've decided to use a 15-byte-long buffer. Don't think it's a recommendation.

# We've used such a value to avoid the situation in which the first readlines() invocation consumes the whole file.

# We want the method to be forced to work harder, and to demonstrate its capabilities.

# There are two nested loops in the code: the outer one uses readlines()'s result to iterate through it, while the inner one prints the lines character by character.


from os import strerror

try:
    ccnt = lcnt = 0
    s = open('/Users/dmitrijvaledinskij/Python/data/zen_of_python.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
