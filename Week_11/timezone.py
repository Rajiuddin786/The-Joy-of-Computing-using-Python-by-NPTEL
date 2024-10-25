from datetime import datetime as dt
import pytz

timezones=pytz.all_timezones

for i in timezones:
    tz=pytz.timezone(i)
    print(f"Time ar {i} is {dt.now(tz)}")