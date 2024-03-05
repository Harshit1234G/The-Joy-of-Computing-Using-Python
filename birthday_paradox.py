import random
import datetime

birthday = []

for _ in range(100):
    year = random.randint(1940, 2023)
    leap = True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False

    month = random.randint(1, 12)

    if month == 2 and leap:
        days = 29

    elif month == 2 and not leap:
        days = 28

    elif month in (1, 3, 5, 7, 8, 10, 12):
        days = 31
    
    else:
        days = 30

    day = random.randint(1, days)
    dd = datetime.date(year, month, day)
    day_of_year = dd.timetuple().tm_yday

    birthday.append(day_of_year)

birthday.sort()
for day in birthday:
    print(day)
