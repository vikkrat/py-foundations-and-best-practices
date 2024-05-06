'''
Create a date object to represent a specific date (December 14, 2023) and a time object to represent a specific time (12:30:15). 
Then, we use datetime.combine to create a new datetime object that represents this specific moment in time.

This method is useful when you have separate date and time components that need to be combined to obtain an exact moment in time.
'''

from datetime import date, time, datetime

# Create a date object for December 14, 2023
specific_date = date(2023, 12, 14)

# Create a time object for 12:30:15
specific_time = time(12, 30, 15)

# Combine the date and time objects to create a datetime object
specific_datetime = datetime.combine(specific_date, specific_time)

# Print the resulting datetime object
print(specific_datetime)