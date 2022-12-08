# Exercise 1
# What do we expect from the readlines() method when the stream is associated with an empty file?

# An empty list (a zero-length list).

# Exercise 2
# What is the following code intended to do?

for line in open("file", "rt"):
    for char in line:
        if char.lower() not in "aeiouy ":
            print(char, end='')

# It copies the file's contents to the console, ignoring all vowels.

# Exercise 3
# You're going to process a bitmap stored in a file named image.png, and you want to read its contents 
# as a whole into a bytearray variable named image. Add a line to the following code to achieve this goal.

# image = bytearray(1024)

try:
    stream = open("image.png", "rb")
    # stream.readinto(image) # Insert a line here.
    image = bytearray(stream.read())
    stream.close()
except IOError:
    print("failed")
else:
    print("success")