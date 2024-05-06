'''
Task 4
--------------------------------------------------------------------------------------------

Within your organization, you are responsible for organizing birthday greetings for colleagues. 
To optimize this process, you need to create a function get_upcoming_birthdays, 
which will help you determine who among your colleagues needs to be greeted. 
The function should return a list of all colleagues whose birthdays are within the next 7 days, including the current day.

You have a list users at your disposal, each element of which contains information about the user's name and their birthday. 
Since colleagues' birthdays may fall on weekends, your function should also take this into account 
and move the greeting date to the next working day if necessary.

Task Requirements:

• The function parameter users is a list of dictionaries, where each dictionary contains keys name (user's name, string) 
  and birthday (birthday, string in the format 'year.month.day').
• The function should determine whose birthdays fall within the next 7 days, including the current day. 
  If the birthday falls on a weekend, the greeting date should be moved to the next Monday.
• The function should return a list of dictionaries, where each dictionary contains information about the user (key name) 
  and the congratulation date (key congratulation_date, data in the format 'year.month.day').

Recommendations for Implementation:

• Assume you have received a list users, where each dictionary contains name (user's name) and birthday 
  (birthday date in the format 'year.month.day'). You should convert the birthday dates from strings to datetime objects. 
  Convert the birthday date from a string to a datetime object - datetime.strptime(user["birthday"], "%Y.%m.%d").date(). 
  Since only the date is needed (without the time), use .date() to get only the date.
• Determine the current system date using datetime.today().date().
• Iterate through the users list and analyze the birthdays of each user (for user in users:).
• Check if the birthday has already passed this year (if birthday_this_year < today). 
  If so, consider the date for the next year.
• Determine the difference between the birthday and the current date to determine birthdays for the next week.
• Check if the birthday falls on a weekend. If so, move the greeting date to the next Monday.
• Create a data structure to store the user names and corresponding greeting dates if the birthday falls within the next week.
• Output the collected data in the form of a list of dictionaries with user names and greeting dates.

Assessment Criteria:

• The correctness of determining birthdays within the next 7 days.
• Proper handling of cases where birthdays fall on weekends.
• Readability and structure of the code.

Example:
• Suppose you have a list users:

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

Using the function get_upcoming_birthdays:

upcoming_birthdays = get_upcoming_birthdays(users)
print("List of greetings for this week:", upcoming_birthdays)

If today is 2024.01.22, the result might be:

[
    {'name': 'John Doe', 'congratulation_date': '2024.01.23'}, 
    {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
]

This list contains information about who and when needs to be congratulated on their birthday.
'''

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Calculate the next birthday for this year
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Check if the birthday falls within the next 7 days
        if (birthday_this_year - today).days <= 7:
            # If the birthday falls on a weekend, move it to the next Monday
            if birthday_this_year.weekday() >= 5:  # Saturday (5) or Sunday (6)
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})

    return upcoming_birthdays

# Test the function
users = [
    {"name": "John Doe", "birthday": "1985.05.10"},
    {"name": "Jane Smith", "birthday": "1990.05.11"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("List of greetings for this week:", upcoming_birthdays)
