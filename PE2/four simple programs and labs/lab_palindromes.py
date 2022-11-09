# palindrome check

str = input("Please enter your string: ")
str = str.replace(" ", "").upper()
crit = False

for i in range(len(str)):
    if str[i] == str[len(str) - i - 1]:
        crit = True
        continue
    crit = False
    if len(str) > 0:
        print("str length = ", len(str), "steps made = ", i + 1)
    break

if len(str) == 0 or not crit:
    print("It's not a palindrome")
else:
    print("It's a palindrome")