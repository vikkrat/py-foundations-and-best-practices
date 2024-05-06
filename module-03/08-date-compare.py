'''
To compare two datetime objects in Python, you can use standard comparison operators such as 
   == (equality), 
   != (inequality), 
   < (less than), 
   > (greater than), 
   <= (less than or equal to), 
   >= (greater than or equal to). 

These operators allow you to compare dates and times to determine whether one datetime object precedes, follows, 
or is exactly the same as another.
'''

from datetime import datetime  # Import the datetime class from the datetime module

# Create two datetime objects representing different dates and times
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Compare the datetime objects using standard comparison operators
print(datetime1 == datetime2)  # Check if datetime1 is equal to datetime2 (False)
print(datetime1 != datetime2)  # Check if datetime1 is not equal to datetime2 (True)
print(datetime1 < datetime2)   # Check if datetime1 is less than datetime2 (True)
print(datetime1 > datetime2)   # Check if datetime1 is greater than datetime2 (False)
