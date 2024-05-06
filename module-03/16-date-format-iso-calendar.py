'''
Also consider the useful isocalendar() method, which is used to get a tuple containing the ISO year, 
week number of the year, and day of the week number according to ISO 8601.

The output of isocalendar() is a tuple (ISO_year, ISO_week, ISO_day_week) where:

• ISO_year is the year in ISO format.
• ISO_week - number of the week of the year according to ISO 8601 (from 1 to 53).
• ISO_day_of_the_week is the day of the week according to ISO 8601, where 1 means Monday and 7 means Sunday.
'''

# Importing the datetime class from the datetime module
from datetime import datetime  

now = datetime.now()  # Obtaining the current date and time

iso_calendar = now.isocalendar()  # Obtaining the ISO calendar information for the current date

# Printing the ISO year, ISO week number, and ISO day of the week
print(f"ISO year: {iso_calendar[0]}, ISO week: {iso_calendar[1]}, ISO day of week: {iso_calendar[2]}")

# iso_calendar[0] retrieves the ISO year from the tuple.
# iso_calendar[1] retrieves the ISO week number from the tuple.
# iso_calendar[2] retrieves the ISO day of the week from the tuple.