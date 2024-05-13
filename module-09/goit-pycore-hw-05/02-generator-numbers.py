'''
Task 2
--------------------------------------------------------------------------------------------

It is necessary to create a function generator_numbers, which will analyze the text, identify 
all valid numbers considered as parts of income, and return them as a generator. Valid numbers 
in the text are written without errors, clearly separated by spaces on both sides. Also, implement 
the function sum_profit, which will use generator_numbers to sum these numbers and calculate the total profit.

Task Requirements:

• The function generator_numbers(text: str) should take a string as an argument and return a generator 
  that iterates through all valid numbers in the text. Valid numbers in the text are considered to be 
  written without errors and clearly separated by spaces on both sides.
• The function sum_profit(text: str, func: Callable) should use the generator_numbers generator to calculate 
  the total sum of the numbers in the input string and take it as an argument when called.

Execution Recommendations:

• Use regular expressions to identify valid numbers in the text, considering that the numbers are clearly 
  separated by spaces.
• Apply the yield construction in the generator_numbers function to create a generator.
• Ensure that sum_profit correctly processes data from generator_numbers and sums all the numbers.

Evaluation Criteria:

• Correctness in identifying and returning valid numbers by the generator_numbers function.
• Correctness in calculating the total sum in sum_profit.
• Code cleanliness, presence of comments, and adherence to the PEP8 coding style.

Usage Example:

text = "The total income of the employee consists of several parts: 1000.01 as the main income, 
        supplemented by additional revenues of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")
Expected Output:

Total income: 1351.46
'''

import re
from typing import Callable, Generator


# This generator function finds and yields valid numbers from the provided text.
# The numbers are clearly separated by spaces and correctly formatted.
def generator_numbers(text: str) -> Generator[float, None, None]:
    # Regular expression to match numbers that are standalone (surrounded by spaces or string boundaries)
    pattern = r'\b\d+\.?\d*\b'
    for match in re.finditer(pattern, text):
        yield float(match.group(0))  # Convert matched string to float and yield


# This function calculates the total sum of all valid numbers identified in the text using the provided generator function.
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))  # Sum up all numbers generated by the generator function

# Test the function
text = "The total income of the employee consists of several parts: 1000.01 as the main income, supplemented by additional revenues of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")