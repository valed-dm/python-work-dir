# Scenario
# A text file contains some text (nothing unusual) but we need to know how often (or how rare)
# each letter appears in the text. Such an analysis may be useful in cryptography,
# so we want to be able to do that in reference to the Latin alphabet.

# Your task is to write a program which:

# asks the user for the input file's name;
# reads the file (if possible) and counts all the Latin letters
# (lower- and upper-case letters are treated as equal)
# prints a simple histogram in alphabetical order (only non-zero counts should be presented)
# Create a test file for the code, and check if your histogram contains valid results.

# Assuming that the test file contains just one line filled with:

# aBc
# samplefile.txt

# the expected output should look as follows:

# a -> 1
# b -> 1
# c -> 1
# output

# Tip: We think that a dictionary is a perfect data collection medium for storing the counts.
# The letters may be keys while the counters can be values.


from os import strerror

# dest = input("Enter the test file path: ")
# test_content = input("Input your test string: ")

# try:
#     fo = open(dest, 'wt')
#     fo.write(test_content)
#     fo.close()
# except IOError as e:
#     print("I/O error occurred: ", strerror(e.errno))

ch_freq = {}

srcname = input("Enter the source file name: ")

try:
    src = open(srcname, 'rt')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)

ch = src.read(1)
while ch != '':
    if ch.isalpha():
        ch = ch.lower()
        if ch not in ch_freq:
            ch_freq[ch] = 1
        else:
            ch_freq[ch] += 1
    ch = src.read(1)

src.close()

print("The original dictionary is : " + str(ch_freq))
print(ch_freq.items())
sorted_dict = dict(sorted(ch_freq.items(), key=lambda item: item[0]))

print("Result dictionary sorted by keys : " + str(sorted_dict))

for key in sorted_dict:
    if ch_freq[key] > 0:
        print(key, '->', ch_freq[key])
