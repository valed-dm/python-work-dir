# Processing text files
# In this lesson we're going to prepare a simple text file with some short, simple content.

# We're going to show you some basic techniques you can utilize to read the file contents
# in order to process them.

# The processing will be very simple - you're going to copy the file's contents to the console,
# and count all the characters the program has read in.

# But remember - our understanding of a text file is very strict.
# In our sense, it's a plain text file - it may contain only text, without any additional decorations
# (formatting, different fonts, etc.).

# That's why you should avoid creating the file using any advanced text processor like MS Word,
# LibreOffice Writer, or something like this. Use the very basics your OS offers: Notepad, vim, gedit, etc.

# If your text files contain some national characters not covered by the standard ASCII charset,
# you may need an additional step. Your open() function invocation may require an argument denoting
# specific text encoding.

# For example, if you're using a Unix/Linux OS configured to use UTF-8 as a system-wide setting,
# the open() function may look as follows:

# stream = open('file.txt', 'rt', encoding='utf-8')


# where the encoding argument has to be set to a value which is a string
# representing proper text encoding (UTF-8, here).

# Consult your OS documentation to find an encoding name adequate to your environment.


# Note

# For the purposes of our experiments with file processing carried out in this section,
# we're going to use a pre-uploaded set of files (i.e., tzop.txt, or text.txt files)
# which you'll be able to work with. If you'd like to work with your own files locally on your machine,
# we strongly encourage you to do so, and to use IDLE (or any other IDE that you may prefer)
# to carry out your own tests.

# /Users/dmitrijvaledinskij/Python/data/zen_of_python.rtf

# Opening tzop.txt in read mode, returning it as a file object:

stream = open("/Users/dmitrijvaledinskij/Python/data/zen_of_python.txt",
              "rt", encoding="utf-8")

print(stream.read())  # printing the content of the file (read(-1) = print all, default value)
