'''
To convert local time to UTC time, you must first assign local time the corresponding time zone, 
and then use the astimezone() method to convert it to UTC:
'''

# Importing necessary modules and classes
from datetime import datetime, timezone, timedelta  

# Defining the local timezone offset (in this case, UTC+2)
local_timezone = timezone(timedelta(hours=2))

# Creating a local time object with the specified timezone
local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# Converting local time to UTC time
utc_time = local_time.astimezone(timezone.utc)

# Printing the UTC time
print(utc_time)  # Output will display the time in UTC. Format: 2023-03-14 10:30:00+00:00





