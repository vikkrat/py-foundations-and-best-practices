'''
ISO date format refers to the international standard for representing dates and times, known as ISO 8601. 
This standard is created by the International Organization for Standardization (ISO) 
and is used to standardize the representation of dates and times worldwide.

The date format in ISO 8601 looks like "YYYY-MM-DD", where:

• YYYY represents the year (e.g., 2023),
• MM represents the month (e.g., 01 for January),
• DD represents the day (e.g., 31).
• The time format in ISO 8601 looks like "HH:MM:SS", where:

• HH represents hours (from 00 to 23),
• MM represents minutes (from 00 to 59),
• SS represents seconds (from 00 to 59, sometimes with additional decimal fractions for microseconds).

The complete representation of date and time in ISO 8601 combines these two formats with a "T" between them, 
for example, "YYYY-MM-DDTHH:MM:SS". 
This separates the date from the time, and the format is easily distinguishable from other representations.

ISO 8601 also supports representations of time zones. For example, "Z" at the end indicates UTC (Coordinated Universal Time), 
and the deviation from UTC can be represented as "+HH:MM" or "-HH:MM". 
The term UTC, which stands for Coordinated Universal Time, 
is the primary time system from which all time zones in the world are regulated. 
It is used as the global time standard, remaining unchanged throughout the year 
and not subject to daylight saving time transitions, unlike many local time zones.

Due to its universality, UTC is widely used in international communications, aviation, astronomy, and other fields. 
Local time zones are often defined as UTC plus or minus a certain number of hours.

The datetime module provides convenient tools for working with dates and times in ISO 8601 format. 
A datetime object can be easily converted to a string in ISO 8601 format using the isoformat() method.
'''

# Import the datetime class from the datetime module
from datetime import datetime  

now = datetime.now()  # Get the current date and time

# Convert the current date and time to ISO 8601 format
iso_format = now.isoformat()
print(iso_format)  # Print the ISO 8601 formatted string

iso_date_string = "2023-03-14T12:39:29.992996"  # Define an ISO 8601 formatted date string

# Convert the ISO 8601 formatted date string to a datetime object
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso)  # Print the datetime object created from the ISO 8601 formatted string


day_of_week = now.isoweekday()  # Calculate the day of the week for the current date

print(f"Today is : {day_of_week}")  # Print the day of the week

