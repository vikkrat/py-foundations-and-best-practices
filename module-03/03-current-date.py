# This line imports the datetime class from the datetime module. The datetime class is used to represent dates and times in Python.
from datetime import datetime

# This line creates a datetime object representing the current date and time. 
# The now() method returns a datetime object with the current date and time information.
current_datetime = datetime.now()

# This line prints the year component of the current_datetime object. 
# The year attribute of a datetime object represents the year.
print(current_datetime.year)

# This line prints the month component of the current_datetime object. 
# The month attribute of a datetime object represents the month (as an integer between 1 and 12).
print(current_datetime.month)

# This line prints the day component of the current_datetime object. 
# The day attribute of a datetime object represents the day of the month.
print(current_datetime.day)

# This line prints the hour component of the current_datetime object. 
# The hour attribute of a datetime object represents the hour (as an integer between 0 and 23).
print(current_datetime.hour)

# This line prints the minute component of the current_datetime object. 
# The minute attribute of a datetime object represents the minute (as an integer between 0 and 59).
print(current_datetime.minute)

# This line prints the second component of the current_datetime object. 
# The second attribute of a datetime object represents the second (as an integer between 0 and 59).
print(current_datetime.second)

# This line prints the microsecond component of the current_datetime object. 
# The microsecond attribute of a datetime object represents the microsecond (as an integer between 0 and 999999).
print(current_datetime.microsecond)

# This line prints the timezone information associated with the current_datetime object. 
# By default, the tzinfo attribute of a datetime object is None, indicating that the timezone is not specified. 
# If you need to work with timezones, you can use the pytz module or the timezone class from the datetime module to specify the timezone.
print(current_datetime.tzinfo)
