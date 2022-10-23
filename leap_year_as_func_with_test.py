def is_year_leap(year):
    if year < 1582:
        #print("Not within the Gregorian calendar period")
        return False
    elif year % 4 != 0:
        #print("Common year")
        return False
    elif year % 100 != 0:
        #print("Leap year")
        return True
    elif year % 400 != 0:
        #print("Common year")
        return False
    else:
        #print("Leap year")
        return True


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "-> ", end="")
    result = is_year_leap(yr)

    if result == test_results[i] and test_results[i]:
        print("OK, this is a 'Leap' year")
    elif result == test_results[i] and not test_results[i]:
        print("OK, this is a 'Common' year")
    else:
        print("Failed")

user_year = int(input("check the year at your choice: "))
if is_year_leap(user_year):
    print("this is a 'Leap' year")
else:
    print("this is a 'Common' year")
