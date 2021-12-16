import datetime

x = datetime.datetime.now()
print(x)  # 2021-12-10 15:20:00.775254

print(x.year)  # 2021
print(x.month)  # 12
print(x.day)  # 10

x = datetime.datetime(2020, 5, 17)
print(x)  # 2020-05-17 00:00:00

"""
The strftime() Method
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
"""

# print("Hello") if(5>2) else print("Bye") # Hello
