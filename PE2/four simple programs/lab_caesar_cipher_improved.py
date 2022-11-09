# Caesar improved cipher.
text = input("Enter your message: ")
while True:
    shift = int(input("Enter your shift (an integer in range 1-25): "))
    if shift >= 1 and shift <= 25:
        break

cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue
    code = ord(char) + shift
    if char.islower():
        if code > ord('z'):
            code -= 26
    else:
        if code > ord('Z'):
            code -= 26
    cipher += chr(code)

print(cipher)

# Sample input:
# abcxyzABCxyz 123
# 2

# Sample output:
# cdezabCDEzab 123

# Sample input:
# The die is cast
# 25

# Sample output:
# Sgd chd hr bzrs