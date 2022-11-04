# Create a fo#r loop that counts from 0 to 10, and prints odd numbers to the screen.
for i in range(11):
    if i % 2:  # True == 1, False == 0
        print(i, end=",")  # odds
for i in range(11):
    if i % 2 == 0:
        print(i, end=";")  # evens

# Create a while loop that counts from 0 to 10, and prints odd numbers to the screen.
x = 1
while x < 11:
    if x % 2:  # True == 1, False == 0
        print(x, end=",")  # odds
    x += 1

# Create a program with a for loop and a break statement.
# The program should iterate over characters in an email address,
# exit the loop when it reaches the @ symbol,
# and print the part before @ on one line.
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

# Create a program with a for loop and a continue statement.
# The program should iterate over a string of digits,
# replace each 0 with x,
# and print the modified string to the screen.
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
