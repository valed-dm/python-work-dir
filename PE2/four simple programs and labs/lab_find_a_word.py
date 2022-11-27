# find a word
# dog
# "vcxzxduybfdsobywuefgas"
# "vcxzxdcybfdstbywuefsas"

# donor
# Nabucodonosor

# donut
# Nabucodonosor

count = 0
cycle = 0

word = input("please, input word: ")
str = input("please, input string: ")

for ch in word:
    cycle += 1
    if str.find(ch) != -1:
        count += 1
    else:
        break

print("count", count)
print("cycle", cycle)

if len(word) == count:
    print("Yes!")
else:
    print("No!")
