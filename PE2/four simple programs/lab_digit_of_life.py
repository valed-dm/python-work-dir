# Some say that the Digit of Life is a digit evaluated using somebody's birthday. 
# It's simple - you just need to sum all the digits of the date. 
# If the result contains more than one digit, 
# you have to repeat the addition until you get exactly one digit. For example:

# 1 January 2017 = 2017 01 01
# 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
# 1 + 2 = 3
# 3 is the digit we searched for and found.

birth_list = list(input('''
Enter the date of your birth in any format:
YYYYMMDD, or YYYYDDMM, or MMDDYYYY: '''))

def list_sum(list):
    sum = 0
    for num in list:
        sum += int(num)
    return sum

dol = list_sum(birth_list)

while len(str(dol)) > 1:
    dol = list_sum(list(str(dol)))

print("Your Digit of Life is: ", dol)

# Sample input:
# 19991229

# Sample output:
# 6


# Sample input:
# 20000101

# Sample output:
# 4