# File handles
# Python assumes that every file is hidden behind an object of an adequate class.

# Of course, it's hard not to ask how to interpret the word adequate.

# Files can be processed in many different ways - some of them depend on the file's contents, 
# some on the programmer's intentions.

# In any case, different files may require different sets of operations, 
# and behave in different ways.

# An object of an adequate class is created when you open the file and annihilate it 
# at the time of closing.

# Between these two events, you can use the object to specify what operations 
# should be performed on a particular stream. 
# The operations you're allowed to use are imposed by the way in which you've opened the file.




# In general, the object comes from one of the classes shown here:


# The origin of objects: IOBase, RawIOBase, BufferedIOBase, TextIOBase


# Note: you never use constructors to bring these objects to life. 
# The only way you obtain them is to invoke the function named open().

# The function analyses the arguments you've provided, 
# and automatically creates the required object.

# If you want to get rid of the object, you invoke the method named close().

# The invocation will sever the connection to the object, and the file and will remove the object.

# For our purposes, we'll concern ourselves only with streams 
# represented by BufferIOBase and TextIOBase objects. 
# You'll understand why soon.





# File handles: continued

# Due to the type of the stream's contents, all the streams 
# are divided into text and binary streams.

# The text streams ones are structured in lines; 
# that is, they contain typographical characters (letters, digits, punctuation, etc.) 
# arranged in rows (lines), as seen with the naked eye when you look at the contents 
# of the file in the editor.

# This file is written (or read) mostly character by character, or line by line.

# The binary streams don't contain text but a sequence of bytes of any value. 
# This sequence can be, for example, an executable program, an image, an audio or a video clip, 
# a database file, etc.

# Because these files don't contain lines, the reads and writes relate to portions of data of any size. 
# Hence the data is read/written byte by byte, or block by block, 
# where the size of the block usually ranges from one to an arbitrarily chosen value.

# Then comes a subtle problem. In Unix/Linux systems, the line ends are marked by 
# a single character named LF (ASCII code 10) designated in Python programs as \n.

# Other operating systems, especially these derived from the prehistoric CP/M system 
# (which applies to Windows family systems, too) use a different convention: 
# the end of line is marked by a pair of characters, CR and LF (ASCII codes 13 and 10) 
# which can be encoded as \r\n.




# Text vs. binary streams concept


# This ambiguity can cause various unpleasant consequences.

# If you create a program responsible for processing a text file, 
# and it is written for Windows, you can recognize the ends of the lines by finding the \r\n 
# characters, but the same program running in a Unix/Linux environment will be completely useless, 
# and vice versa: the program written for Unix/Linux systems might be useless in Windows.

# Such undesirable features of the program, which prevent or hinder the use of the program 
# in different environments, are called non-portability.

# Similarly, the trait of the program allowing execution in different environments 
# is called portability. A program endowed with such a trait is called a portable program.


# File handles: continued

# Since portability issues were (and still are) very serious, 
# a decision was made to definitely resolve the issue in a way that doesn't engage 
# the developer's attention.


# Text vs. binary streams concept


# It was done at the level of classes, which are responsible for reading and writing 
# characters to and from the stream. It works in the following way:

# when the stream is open and it's advised that the data in the associated file 
# will be processed as text (or there is no such advisory at all), 
# it is switched into text mode;

# during reading/writing of lines from/to the associated file, 
# nothing special occurs in the Unix environment, 
# but when the same operations are performed in the Windows environment, 
# a process called a translation of newline characters occurs: 
# when you read a line from the file, every pair of \r\n characters is replaced with a 
# single \n character, and vice versa; during write operations, 
# every \n character is replaced with a pair of \r\n characters;

# the mechanism is completely transparent to the program, which can be written 
# as if it was intended for processing Unix/Linux text files only; 
# the source code run in a Windows environment will work properly, too;

# when the stream is open and it's advised to do so, 
# its contents are taken as-is, without any conversion - no bytes are added or omitted.


# Opening the streams

# The opening of the stream is performed by a function which can be invoked in the following way:

file = ""

stream = open(file, mode = 'r', encoding = None)


# Let's analyze it:

# the name of the function (open) speaks for itself; 
# if the opening is successful, the function returns a stream object; 
# otherwise, an exception is raised (e.g., FileNotFoundError 
# if the file you're going to read doesn't exist);

# the first parameter of the function (file) specifies the name of the file 
# to be associated with the stream;

# the second parameter (mode) specifies the open mode used for the stream; 
# it's a string filled with a sequence of characters, 
# and each of them has its own special meaning (more details soon);

# the third parameter (encoding) specifies the encoding type 
# (e.g., UTF-8 when working with text files)

# the opening must be the very first operation performed on the stream.
# Note: the mode and encoding arguments may be omitted - 
# their default values are assumed then. 
# The default opening mode is reading in text mode, 
# while the default encoding depends on the platform used.

# Let us now present you with the most important and useful open modes. Ready?