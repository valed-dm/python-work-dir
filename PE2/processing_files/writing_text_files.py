# Dealing with text files: write()
# Writing text files seems to be simpler, as in fact there is one method that can be used 
# to perform such a task.

# The method is named write() and it expects just one argument - 
# a string that will be transferred to an open file 
# (don't forget - the open mode should reflect the way in which the data is transferred - 
# writing a file opened in read mode won't succeed).

# No newline character is added to the write()'s argument, 
# so you have to add it yourself if you want the file to be filled with a number of lines.

# The example in the editor shows a very simple code that creates a file named newtext.txt 
# (note: the open mode w ensures that the file will be created from scratch, 
# even if it exists and contains data) and then puts ten lines into it.

# The string to be recorded consists of the word line, 
# followed by the line number. We've decided to write the string's contents character by character 
# (this is done by the inner for loop) but you're not obliged to do it in this way.

# We just wanted to show you that write() is able to operate on single characters.

# The code creates a file filled with the following text:

# line #1
# line #2
# line #3
# line #4
# line #5
# line #6
# line #7
# line #8
# line #9
# line #10
# output


from os import strerror

try:
    # A new file (newtext.txt) is created.
    fo = open('/Users/dmitrijvaledinskij/Python/data/newtext.txt', 'wt')
    for i in range(10):
        s = "line #" + str(i+1) + "\n"
        for ch in s:
            fo.write(ch)
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


# Can you print the file's contents to the console?
# We encourage you to test the behavior of the write() method locally on your machine.


try:
    ccnt = lcnt = 0
    for line in open('/Users/dmitrijvaledinskij/Python/data/newtext.txt', 'rt'):
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


# Dealing with text files: continued
# Look at the example in the editor. We've modified the previous code to 
# write whole lines to the text file.

# The contents of the newly created file are the same.

# Note: you can use the same method to write to the stderr stream, but don't try to open it, 
# as it's always open implicitly.

# For example, if you want to send a message string to stderr to distinguish it from 
# normal program output, it may look like this:


# import sys
# sys.stderr.write("My Error message added")
from os import strerror

try:
    fo = open('newtext_by_whole_lines.txt', 'wt')
    for i in range(10):
        fo.write("line #" + str(i+1) + "\n")
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
