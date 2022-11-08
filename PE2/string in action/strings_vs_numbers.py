itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print("number to string: num_str = str(number)")
print(si + ' concatenation ' + sf)

# The reverse transformation (string-number) is possible when and only 
# when the string represents a valid number. 
# If the condition is not met, expect a ValueError exception.
# Use the int() function if you want to get an integer, 
# and float() if you need a floating-point value.

si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print("str_num = int(str), float(str)")
print(itg + flt)