#
#   A date object represents a date (year, month and day) in an idealized calendar.

from datetime import date, timedelta

# Obtaining today's date

today = date.today()
print(today.isoformat())

# set a custom date

myBirthday = date(today.year, 7, 14)

randomDay = date(2014, 7, 14)

print(randomDay)

# returns a modified date based on another, can do the same with month and day
randomDay2 = randomDay.replace(year=2015)
print(randomDay, randomDay2)

# weekday returns the day of the week, where Monday is 0 and Sunday is 6
# isoweekday is the same but Monday is 1 and Sunday is 7

print(randomDay.weekday(), randomDay.isoweekday())

# You can subtract dates from dates to obtain a timedelta, or timedelta from dates to obtain another date

fiveDays = timedelta(days=5)
result = randomDay - fiveDays

print(result, randomDay, fiveDays)

result = randomDay2 - randomDay

print(result, randomDay2, randomDay)

# You can access the year, month, and day of a date

print("Year: " + str(randomDay.year) + " Month: " + str(randomDay.month) + " Day: " + str(randomDay.day))