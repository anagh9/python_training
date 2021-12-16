# For working with date and time both
import datetime
t = datetime.time(9, 30, 43, 100000)
print(t.hour)  # 9
print(t.minute)  # 30
print(t.second)  # 43
print(t.microsecond)  # 100000

date_time = datetime.datetime(2021, 12, 10, 21, 47, 12, 10000)
print(date_time)  # 2021-12-10 21:47:12.010000

tdelta = datetime.timedelta(hours=12, minutes=30)
print(date_time+tdelta)  # 2021-12-11 10:17:12.010000

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)  # 2021-12-10 21:51:43.979557
print(dt_now)  # 2021-12-10 21:51:43.979557
print(dt_utcnow)  # 2021-12-10 21:51:43.979557
