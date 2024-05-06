'''
To convert a time from UTC to another time zone, you need to define a timezone object with the appropriate offset. 
For example, to convert a UTC time to a time corresponding to US Eastern Time Zone (UTC-5 hours), 
you can do the following:
'''

# Importing necessary modules and classes
from datetime import datetime, timezone, timedelta  

# Obtaining the current UTC time
utc_time = datetime.now(timezone.utc)

# Converting UTC time to Eastern Time (ET)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))

# Printing the Eastern Time
print(eastern_time)




