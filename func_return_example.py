def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False


print(is_int(5)) # True
print(is_int(5.0)) # False
print(is_int("5")) # None
