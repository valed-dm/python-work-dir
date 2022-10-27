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
    except ValueError:
        print('I do not know what to do. Try again')
        data_entered()
        continue
    except ZeroDivisionError:
        print('Division by zero is not allowed in our Universe.')
        data_entered()
        continue
    except:
        print('Something strange has happened here... Sorry!')
        data_entered()
        continue