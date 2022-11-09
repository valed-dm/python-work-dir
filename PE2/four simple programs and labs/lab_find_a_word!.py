# find a word
count = 0
crit = True

word = "dog"
str1 = "vcxzxduybfdsobywuefgas"
str2 = "vcxzxdcybfdstbywuefsas"

while crit:
    for ch in word:
        if str1.find(ch) != -1:
            crit =  True
            count += 1
            continue
    count = 0
    break

if count !=0:
    print("Yes!")

print("No!")