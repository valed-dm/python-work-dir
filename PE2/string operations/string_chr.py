# Demonstrating the chr() function.
# If you know the code point (number) and want to get the corresponding character, you can use a function named chr().

# print(chr(937))
# print(chr(948))
# print(chr(46))

unicode = []
for i in range(1000):
    unicode.append(str(i) + ': ' + str(chr(i)))

for j in range(100):
    print(j, unicode[j*10:j*10+10])