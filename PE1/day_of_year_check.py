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


def day_of_year(year, month, day):
    if days_in_month(year, month) == day:
        return (str(year) + "-" + str(month) + "-" + str(day))


print(day_of_year(1990, 2, 29))
