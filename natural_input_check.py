# try:
#     value = int(input('Enter a natural number: '))
#     print('The reciprocal of', value, 'is', 1/value)
# except:
#     print('I do not know what to do.')
input_data = ""
def data_entered():
    print("you've entered: ", input_data)

while True:
    try:
        input_data = input('Enter a natural number: ')
        value = int(input_data)
        print('The reciprocal of', value, 'is', 1/value)
        break
    except ValueError: #  In general, this exception is raised when a function (like int() or float()) 
                       # receives an argument of a proper type, but its value is unacceptable.
        print('I do not know what to do. Try again')
        data_entered()
        continue
    except ZeroDivisionError: # /, //, and %.
        print('Division by zero is not allowed in our Universe.')
        data_entered()
        continue
    except:
        print('Something strange has happened here... Sorry!')
        data_entered()
        continue

# TypeError
# short_list = [1]
# one_value = short_list[0.5]

# AttributeError
short_list = [1]
short_list.append(2)
short_list.depend(3)

# SyntaxError
# This exception is raised when the control reaches a line of code which violates Python's grammar. 
# It may sound strange, but some errors of this kind cannot be identified without first running the code. 
# This kind of behavior is typical of interpreted languages – the interpreter always works in a hurry 
# and has no time to scan the whole source code. 
# It is content with checking the code which is currently being run. 
# An example of such a category of issues will be presented very soon.

# It's a bad idea to handle this exception in your programs. 
# You should produce code that is free of syntax errors, instead of masking the faults you’ve caused.
