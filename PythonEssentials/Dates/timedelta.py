#
#   A timedelta object represent a duration, the difference between two dates or times
#   Only days, seconds and microseconds are stored internally
#
#   datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

from datetime import timedelta

year = timedelta(days=365)

print(year.total_seconds())

ten_years = 10 * year

print(ten_years, ten_years.days // 365)

nine_years = ten_years - year

print(nine_years, nine_years.days // 365)

minute = timedelta(seconds=60)

print(year-minute)