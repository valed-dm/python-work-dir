# Location: BaseException ← Exception ← AssertionError

# Description: a concrete exception raised by the assert instruction when its argument 
# evaluates to False, None, 0, or an empty string

from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))

# We must be sure that angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))