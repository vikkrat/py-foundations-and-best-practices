'''
The strptime method in Python is used to convert strings into datetime objects. 
This method is the opposite of strftime, which converts datetime objects to strings. 
strptime allows you to parse strings containing date and/or time and convert them 
into structured datetime objects using a specified format.

The syntax of the strptime method is as follows:
datetime_object = datetime.strptime(string, format)

where:
     string - a string that contains a date and/or time.
     format - a format string that specifies how to parse the string.


The formatting codes for strptime are the same as for strftime. 
For example, %Y represents a four-digit year, %m represents a two-digit month, and so on.
'''

# Import the datetime class from the datetime module
from datetime import datetime  

date_string = "2023.03.14"  # Define a date string in the format "YYYY.MM.DD"

# Use strptime() to parse the date string into a datetime object
# The second argument "%Y.%m.%d" specifies the format of the date string
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")

# Print the datetime object
print(datetime_object) # Format like: 2023-03-14 00:00:00
