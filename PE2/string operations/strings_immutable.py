alphabet = "abcdefghijklmnopqrstuvwxyz"

# del alphabet[0] # TypeError
# alphabet.append("A") # AttributeError
# alphabet.insert(0, "A") # AttributeError

# del alphabet
# print(alphabet) # NameError: name 'alphabet' is not defined

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)
