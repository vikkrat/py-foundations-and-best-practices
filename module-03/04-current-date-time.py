# Import the datetime class from the datetime module
from datetime import datetime  

# Create a datetime object representing the current date and time
current_datetime = datetime.now()  

# Print the date component of the current datetime object
print(current_datetime.date()) # Format like: 2024-05-06

# Print the time component of the current datetime object
print(current_datetime.time()) # Format like: 02:42:40.141987
