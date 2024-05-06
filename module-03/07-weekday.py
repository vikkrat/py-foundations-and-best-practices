'''
In Python, the weekday() method is a part of the datetime class, which is used to represent dates and times. 
This method returns the day of the week as an integer, where Monday is represented by 0, Tuesday by 1, and so on, 
with Sunday represented by 6.

For example:

Monday: 0
Tuesday: 1
Wednesday: 2
Thursday: 3
Friday: 4
Saturday: 5
Sunday: 6

You can call the weekday() method on a datetime object to get the day of the week for that particular date and time. 
This method is useful for tasks such as determining which day of the week a specific date falls on or performing 
conditional logic based on the day of the week.
'''


# Import the datetime class from the datetime module
from datetime import datetime  

# Create a datetime object representing the current date and time
now = datetime.now()  

# Calculate the day of the week for the current datetime object
day_of_week = now.weekday()  

# Print the day of the week using an f-string
print(f"Today is : {day_of_week}")  