def read_int(prompt, min, max):
    while True:
        try:
            user_input = int(input(prompt))

            if not (user_input >= min and user_input <= max):
                print('Error: the value is not within permitted range (' + str(min) + '..' + str(max) + ')')
                continue
            else:
                break

        except ValueError:
            print('Error: wrong input')
            continue
        except:
            print('Error: unexpected exception')

    return int(user_input)

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
