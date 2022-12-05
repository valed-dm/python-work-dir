# from math import pi, radians, degrees, sin, cos, tan, asin

# ad = 90
# ar = radians(ad)
# ad = degrees(ar)

# print(ad == 90.)
# print(ar == pi / 2.)
# print(sin(ar) / cos(ar) == tan(ar))
# print(asin(sin(ar)) == ar)

# Another group of the math's functions is formed by functions which are connected with exponentiation:
# e → a constant with a value that is an approximation of Euler's number (e)
# exp(x) → finding the value of ex;
# log(x) → the natural logarithm of x
# log(x, b) → the logarithm of x to base b
# log10(x) → the decimal logarithm of x (more precise than log(x, 10))
# log2(x) → the binary logarithm of x (more precise than log(x, 2))
# Note: the pow() function:

# pow(x, y) → finding the value of x in power of y (mind the domains)
# This is a built-in function, and doesn't have to be imported.

# Look at the code in the editor. Can you predict its output?

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))
print(e)

# output must be ?:
# False
# True
# True

# The last group consists of some general-purpose functions like:
# ceil(x) → the ceiling of x (the smallest integer greater than or equal to x)
# floor(x) → the floor of x (the largest integer less than or equal to x)
# trunc(x) → the value of x truncated to an integer (be careful - it's not an equivalent either of ceil or floor)
# factorial(x) → returns x! (x has to be an integral and not a negative)
# hypot(x, y) → returns the length of the hypotenuse of a right-angle triangle with the leg lengths equal to x and y (the same as sqrt(pow(x, 2) + pow(y, 2)) but more precise)
# Look at the code in the editor. Analyze the program carefully.

# It demonstrates the fundamental differences between ceil(), floor() and trunc().

from math import ceil, floor, trunc, hypot, factorial

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))
print(hypot(3, 4))
print(factorial(5))