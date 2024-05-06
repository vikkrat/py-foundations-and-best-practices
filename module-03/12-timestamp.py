'''
In the context of programming and data processing, the term "timestamp" is used to indicate a specific moment in time. 
It is typically represented as the number of seconds (or milliseconds/microseconds in some systems) 
since a certain starting date, most commonly January 1, 1970, in UTC, the Greenwich Mean Time zone. 
We'll discuss UTC in more detail a little later. For now, the timestamp is just an accepted constant for us, 
and it doesn't signify anything special. People simply started counting time in seconds from this moment for convenience, 
and it turned out to be very handy. It's a standard way of representing time in many operating systems and programming languages.

Since comparing two numbers is always easier and faster than comparing complex date and time structures, 
you'll encounter the use of timestamps in programming, databases, event logging, and when storing information about moments in time.

☝️ A timestamp is a universal way of representing time because it's independent of time zones and calendar systems.

In Python, you can convert a datetime object to a timestamp and vice versa. Converting a datetime to a timestamp.
'''

# Import the datetime class from the datetime module
from datetime import datetime  

# Get the current date and time
now = datetime.now()

# Convert the datetime object 'now' to a timestamp
timestamp = datetime.timestamp(now)

# Print the timestamp
print(timestamp) # Format like: 1714993693.905508

# Convert the timestamp back to a datetime object
dt_object = datetime.fromtimestamp(timestamp)

# Print the datetime object
print(dt_object) # Format like: 2024-05-06 13:09:18.348755