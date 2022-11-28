# The third program shows a simple method allowing you to input a line filled with numbers, 
# and to process them easily. 
# Note: the routine input() function, combined together with the int() or float() functions, 
# is unsuitable for this purpose.

# The processing will be extremely easy - we want the numbers to be summed.

# Numbers Processor.

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
print("strings", strings)
total = 0
try:
    if len(strings) == 0:
        print("No numbers were entered")
    else:
        for substr in strings:
            total += float(substr)
            print(total)
        print("The total is:", total)
except:
    print(substr, "is not a number.")
