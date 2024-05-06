'''
When we need to display the date and time in a human-readable format, we use the strftime method. 
It is applied when recording timestamps in log files, displaying dates and times on web pages 
or user interfaces, and formatting dates for storage in databases.

So, the strftime method is used to format datetime objects into strings using specific format codes. 
This method allows us to represent the date and time in a readable format or in a format that meets specific requirements.

The syntax of the strftime method looks like this:
datetime_object.strftime(format)
'''

'''
Each code in the format string begins with the % character 
and represents a specific component of the date or time. Here are some of the most used codes:

Code	 | Description	                             | Example
----------------------------------------------------------------
%Y	       Four-digit year	                           2023
%y	       Two-digit year	                           23
%m	       Month as a number	                       03
%d	       Day of the month as a number	               14
%H	       Hour (24-hour format)	                   15
%I	       Hour (12-hour format)	                   03
%M	       Minutes	                                   05
%S	       Seconds	                                   09
%A	       Full name of the day of the week	           Tuesday
%a	       Abbreviated name of the day of the week	   Tue
%B	       Full name of the month	                   March
%b	       Abbreviated name of the month	           Mar
%p	       AM or PM for 12-hour format	               AM
'''

# Import the datetime class from the datetime module
from datetime import datetime

now = datetime.now()  # Get the current date and time

# Format the date and time as "YYYY-MM-DD HH:MM:SS"
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date) # Format like: 2024-05-06 13:18:06

# Format the date as "Day of the week, Day Month Year"
formatted_date_only = now.strftime("%A, %d %B %Y")
print(formatted_date_only) # Format like: Monday, 06 May 2024

# Format the time as "HH:MM AM/PM"
formatted_time_only = now.strftime("%I:%M %p")
print(formatted_time_only) # Format like: 01:18 PM

# Format the date as "Day.Month.Year"
formatted_date_only = now.strftime("%d.%m.%Y")
print(formatted_date_only) # Format like: 06.05.2024


