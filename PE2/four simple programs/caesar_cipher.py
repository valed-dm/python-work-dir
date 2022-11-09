# The first problem we want to show you is called the Caesar cipher - 
# more details here: https://en.wikipedia.org/wiki/Caesar_cipher.

# This cipher was (probably) invented and used by Gaius Julius Caesar 
# and his troops during the Gallic Wars. The idea is rather simple - 
# every letter of the message is replaced by its nearest consequent 
# (A becomes B, B becomes C, and so on). 
# The only exception is Z, which becomes A.

# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)
