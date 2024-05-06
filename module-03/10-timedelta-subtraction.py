'''
Two datetime objects seventh_day_2019 and seventh_day_2020 are created, representing January 7th, 2019, and January 7th, 2020, both at 2 PM.
The difference between seventh_day_2020 and seventh_day_2019 is calculated using the subtraction operator -, resulting in a timedelta object representing the difference in time between the two dates.
The difference is printed, showing that it is 365 days.
The total_seconds() method is called on the timedelta object difference to calculate the total number of seconds in the difference. 
This method returns the total duration of the timedelta object in seconds, which is printed.
'''

# Import the datetime class from the datetime module
from datetime import datetime, timedelta 

# Create datetime objects for the 7th day of January in 2019 and 2020, both at 2 PM
seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

# Calculate the difference between the two datetime objects
difference = seventh_day_2020 - seventh_day_2019

# Print the difference
print(difference)  # Output: 365 days, 0:00:00

# Calculate the total number of seconds in the difference
print(difference.total_seconds())  # Output: 31536000.0


'''
The maximum range for timedelta is limited to about 9999 years, 
which is more than enough for most applications. 
Timedelta objects can be created to get a date/time that is far from the original.
'''

now = datetime.now()
future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
print(future_date)

# ----------------------------------------------------------------

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00