'''
To display the date in UTC format, you can do this by adding information 
about the time zone to the datetime object.
'''

# Importing the datetime class and timezone from the datetime module
from datetime import datetime, timezone, timedelta 

local_now = datetime.now()  # Obtaining the current date and time in the local timezone
utc_now = datetime.now(timezone.utc)  # Obtaining the current date and time in Coordinated Universal Time (UTC)

# Printing the current date and time in the local timezone
print(local_now) # Format like: 2024-05-06 13:41:36.052772

# Printing the current date and time in Coordinated Universal Time (UTC)
print(utc_now) # Format like: 2024-05-06 11:41:36.052772+00:00

'''
The ISO 8601 standard also supports time zones. 
In Python, this can be done by adding timezone information to the datetime object:
'''

# Defining the timezone offset (in this case, UTC+2 hours)
timezone_offset = timezone(timedelta(hours=2))

# Creating a datetime object with the specified date, time, and timezone offset
timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)

# Converting the datetime object to ISO 8601 formatted string with timezone information
iso_format_with_timezone = timezone_datetime.isoformat()

# Printing the ISO 8601 formatted string with timezone information
print(iso_format_with_timezone)




