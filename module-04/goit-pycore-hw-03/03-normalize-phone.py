'''
Task 3
--------------------------------------------------------------------------------------------

In your company, an active marketing campaign is conducted using SMS mailings. 
For this purpose, you collect customer phone numbers from the database, 
but often encounter the issue that the numbers are in various formats. 

For example:

"+38(050)123-32-34"
"0503451234"
"(050)8889900"
"38050-111-22-22"
"38050 111 22 11"

Your mailing service can effectively send messages only when phone numbers are in the correct format. 
Therefore, you need a function that automatically normalizes phone numbers to the required format, 
removing all unnecessary characters and adding the country's international code if necessary.

Develop a function normalize_phone(phone_number) that normalizes phone numbers to a standard format, 
leaving only digits and the '+' symbol at the beginning. 
The function takes one argument - a string with the phone number in any format and converts it to the standard format, 
leaving only digits and the '+' symbol. 
If the number does not contain an international code, the function automatically adds the '+38' code (for Ukraine). 
This ensures that all numbers are suitable for sending SMS.

Requirements for the task:

• The function parameter phone_number is a string with phone numbers in various formats.
• The function removes all characters except digits and the '+' symbol.
• If the international code is missing, the function adds the '+38' code. This accounts for cases where the number starts with '380' (only '+' is added) and when the number starts without a code ('+38' is added).
• The function returns the normalized phone number as a string.

Recommendations for implementation:

• Use the re module for regular expressions to remove unnecessary characters.
• Check if the number starts with '+', and adjust the prefix according to the instructions.
• Remove all characters except digits and '+ from the phone number.
• Do not forget to return the normalized phone number from the function.

Evaluation criteria:

• Correct functioning of the function: the function should correctly handle different formats of numbers, 
  taking into account the presence or absence of the international code.
• Readability of the code: the code should be clean, well-organized, and well-documented.
• Proper use of regular expressions to remove unnecessary characters and format the number.

Example usage:

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS mailings:", sanitized_numbers)

As a result, you should get a list of numbers in the standard format, ready for use in SMS mailings.

Normalized phone numbers for SMS mailings: 
[
    '+380671234567', 
    '+380952345678', 
    '+380441234567', 
    '+380501234567', 
    '+380501233234', 
    '+380503451234', 
    '+380508889900', 
    '+380501112222', 
    '+380501112211'
]
'''

import re

def normalize_phone(phone_number):
    # Remove all characters except digits and '+'
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)

    # Add '+38' if international code is missing
    if not cleaned_number.startswith('+'):
        cleaned_number = '+38' + cleaned_number

    return cleaned_number

# Test data
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Test the function
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

# Print normalized phone numbers
print("Normalized phone numbers for SMS mailings:", sanitized_numbers)
