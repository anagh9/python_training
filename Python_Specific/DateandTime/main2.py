import datetime

# Creating Date
d = datetime.date(2016, 7, 24)  # Pass Single digit
print(d)  # 2016-07-24

today = datetime.date.today()
print(today)  # 2021-12-10
print(today.year)  # 2021
print(today.month)  # 12
print(today.day)  # 10
print(today.weekday())  # 4 -> Friday      # Monday 0 Sunday 6
print(today.isoweekday())  # 5 -> Friday   # Monday 1 Sunday 7

# Creating timedelta 7 day after ago
tdelta = datetime.timedelta(days=7)
print(today + tdelta)  # 2021-12-17

# Creating timedelta 7 day before ago
print(today - tdelta)  # 2021-12-17

# date2 = date1 + timedelta
# timedelta = date1 + date2


# Calculate Age

bday = datetime.date(2022, 9, 24)
till_bday = bday - today
print(till_bday.total_seconds())
