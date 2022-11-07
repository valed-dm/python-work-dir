# The parameterless method named isalnum() checks if the string contains only digits or alphabetical characters (letters), 
# and returns True or False according to the result.

# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

print()

t = 'Six lambdas'
print(t.isalnum())
# Hint: the cause of the first result is a space - it's neither a digit nor a letter.

t = 'ΑβΓδ'
print(t.isalnum())

t = '20E1'
print(t.isalnum())