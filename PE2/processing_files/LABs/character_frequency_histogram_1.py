# Scenario
# The previous code needs to be improved. It's okay, but it has to be better.

# Your task is to make some amendments, which generate the following results:

# the output histogram will be sorted based on the characters' frequency
# (the bigger counter should be presented first)
# the histogram should be sent to a file with the same name as the input one,
# but with the suffix '.hist' (it should be concatenated to the original name)
# Assuming that the input file contains just one line filled with:

# cBabAa
# samplefile.txt

# the expected output should look as follows:

# a -> 3
# b -> 2
# c -> 1
# output

# Tip: Use a lambda to change the sort order.

from os import strerror

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

# print("The original dictionary is : " + str(ch_freq))
# print(ch_freq.items())

sorted_dict = dict(
    sorted(ch_freq.items(), key=lambda item: item[1], reverse=True))

# print("Result dictionary sorted by keys : " + str(sorted_dict))

for key in sorted_dict:
    if ch_freq[key] > 0:
        print(key, '->', ch_freq[key])


print('--------------------------')

hist_path = srcname + '.hist'
dict = list(sorted_dict.items())
# print(dict)

try:
    fo = open(hist_path, 'wt')
    for i in range(len(sorted_dict)):
        fo.write(str(dict[i][0]) + ': --->  ' + str(dict[i][1]) + "\n")
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


try:
    s = open(hist_path, 'rt')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)

# printing the content of the file (read(-1) = print all, default value)
print('Character frequency histogram:\n' + hist_path)
print(s.read())
s.close()
