i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)



# Both loops, while and for, have one interesting (and rarely used) feature.
# As you may have suspected, loops may have the else branch too, like ifs.
# The loop's else branch is always executed once, regardless of whether the loop has entered its body or not.

for i in range(5):
    print(i)
else:
    print("else:", i)

i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)