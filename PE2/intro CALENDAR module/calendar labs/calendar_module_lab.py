# Scenario
# During this course, we looked at the Calendar class a bit.
# Your task is to extend its functionality with a new method called count_weekday_in_year,
# which takes a year and a weekday as parameters, and then returns
# the number of occurrences of a specific weekday in the year.

# Use the following tips:

# Create a class called MyCalendar that extends the Calendar class;
# create the count_weekday_in_year method with the year and weekday parameters.
# The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday.
# The method should return the number of days as an integer;
# in your implementation, use the monthdays2calendar method of the Calendar class.
# The following are the expected results:

# Sample arguments

# year=2019, weekday=0

# Expected output

# 52


# Sample arguments

# year=2000, weekday=6

# Expected output

# 53

import calendar


class MyCalendar(calendar.Calendar):

    def count_weekday_in_year(self, year, weekday):
        counter = 0
        for i in range(12):
            for data in super().monthdays2calendar(year, i+1):
                for day in data:
                    if day[0] != 0 and weekday == day[1]:
                        counter += 1

        return counter


cal = MyCalendar()

print('day of the week --> 6 <-- in the year --> 2000 <-- was encountered -->', cal.count_weekday_in_year(year=2000, weekday=6), '<-- times')

print('----------------')

print('range 1922 - 2022:\nday of the week --> 6 <-- was encountered --> 53 <-- times in a year:')

for year in range(1922, 2022):
    if cal.count_weekday_in_year(year, 6) == 53:
        print(year, end=' ')
