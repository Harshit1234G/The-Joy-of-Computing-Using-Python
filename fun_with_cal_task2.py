from datetime import datetime as dt
import pytz

print(f"Current time in local time zone {dt.now()}")
for zone in pytz.all_timezones:
    print(f"Current time in {zone} is {dt.now(tz=pytz.timezone(zone))}")