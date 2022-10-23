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


def days_in_month(year, month):
    days = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year < 1582:
        return
    if month > 12 or month < 1:
        return
    if month != 2:
        return days[month - 1]
    elif is_year_leap(year):
        return 29
    else:
        return 28


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

user_year = int(input("enter a year at your choice: "))
user_month = int(input("enter a month to get days qty: "))
print(days_in_month(user_year, user_month))
