# anagrams
str1_list = []
str2_list = []
crit = False

str1 = input("Please, enter first string: ")
str2 = input("Please, enter second string: ")
str1 = str1.replace(" ", "").upper()
str2 = str2.replace(" ", "").upper()

for ch in str1:
    str1_list.append(ch)
for ch in str2:
    str2_list.append(ch)

str1_list.sort()
str2_list.sort()

if len(str1_list) == len(str2_list) and len(str1) != 0 and len(str2) != 0:
    for i in range(len(str1_list)):
        if str1_list[i] == str2_list[i]:
            crit = True
        else:
            crit = False
            break

if crit:
    print("Anagrams")
else:
    print("Not anagrams")

# Sample input:
# Listen
# Silent

# Sample output:
# Anagrams


# Sample input:
# modern
# norman

# Sample output:
# Not anagrams