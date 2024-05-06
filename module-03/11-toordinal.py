'''
But if you need to do calculations or comparisons based on a sequence of dates, 
for example to determine the number of days between two dates.

We can use the toordinal() method, which returns the ordinal number of the day, 
taking into account the number of days since January 1 of the year 1 AD 
(that is, since the beginning of the Christian calendar). 
This method converts a datetime object to an integer representing the sequence number of the given day.
'''

# Import the datetime class from the datetime module
from datetime import datetime  

# Create a datetime object representing December 18, 2023
date = datetime(year=2023, month=12, day=18)

# Retrieve the ordinal number representing the date
ordinal_number = date.toordinal()

# Print the date and its corresponding ordinal number
print(f"The serial number of the date {date} is {ordinal_number}")


'''
For example, we want to determine how many full days passed when Napoleon burned Moscow, 
and this happened on September 14, 1812
'''

# Create a datetime object representing September 14, 1812 (when Napoleon burned Moscow)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Get the current date and time
current_date = datetime.now()

# Calculate the number of days elapsed since Napoleon burned Moscow
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()

# Print the number of days since the event
print(f"The number of days elapsed since Napoleon burned Moscow is: {days_since}")
