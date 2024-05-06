'''
Task 1
--------------------------------------------------------------------------------------------

Create a function get_days_from_today(date), which calculates the number of days between the given date and the current date.

Task Requirements:

• The function takes one parameter: date - a string representing the date in the format 'YYYY-MM-DD' (for example, '2020-10-09').
• The function returns an integer indicating the number of days from the given date to the current one. 
If the given date is later than the current one, the result should be negative.
• Only days should be considered in the calculations, ignoring the time (hours, minutes, seconds).
• Use the Python datetime module to work with dates.

Recommendations for Implementation:

• Import the datetime module.
• Convert the date string in the format 'YYYY-MM-DD' into a datetime object.
• Get the current date using datetime.today().
• Calculate the difference between the current date and the given date.
• Return the difference in days as an integer.

Evaluation Criteria:

• Function correctness: the function should accurately calculate the number of days between the dates.
• Exception handling: the function should handle incorrect input data formats.
• Code readability: the code should be clean and well-documented.

Example:

If today is May 5, 2021, calling get_days_from_today("2021-10-09") should return 157, 
as October 9, 2021, is 157 days later than May 5, 2021.
'''

from datetime import datetime

def get_days_from_today(date):
    try:
        # Convert date string to a datetime object
        given_date = datetime.strptime(date, '%Y-%m-%d')
        # Get current date
        current_date = datetime.today()
        # Calculate the difference in days
        days_difference = (current_date - given_date).days
        return days_difference
    except ValueError:
        # Handle invalid date format
        print("Error: Invalid date format. Please provide date in YYYY-MM-DD format.")
        return None

# Test the function
today = datetime.today().strftime('%Y-%m-%d')
print("Today's date:", today)
print("Number of days from '2021-10-09' to today:", get_days_from_today("2021-10-09"))
