'''
Task 2
--------------------------------------------------------------------------------------------

To win the jackpot in a lottery, a match of several numbers on a lottery ticket with randomly drawn numbers 
within a certain range during the next draw is required. 
For example, you need to guess six numbers from 1 to 49 or five numbers from 1 to 36, and so on.

You need to write a function get_numbers_ticket(min, max, quantity) that will help generate a set of unique random numbers 
for such lotteries. It should return a random set of numbers within the specified parameters, 
where all random numbers in the set should be unique.

Requirements for the task:

Function parameters:

• min - the minimum possible number in the set (no less than 1).
• max - the maximum possible number in the set (no more than 1000).
• quantity - the number of numbers to choose (values between min and max).
The function generates the specified number of unique numbers in the given range.
The function returns a list of randomly selected, sorted numbers. The numbers in the set should not repeat. If the parameters do not meet the specified constraints, the function returns an empty list.

Recommendations for implementation:

• Ensure that the input parameters meet the specified constraints.
• Use the random module to generate random numbers.
• Use a set or another mechanism to ensure the uniqueness of numbers.
• Remember that the get_numbers_ticket function returns a sorted list of unique numbers.

Evaluation criteria:

• Validity of input data: the function should validate the correctness of the parameters.
• Uniqueness of the result: all numbers in the output should be unique.
• Compliance with requirements: the result should be in the form of a sorted list.
• Code readability: the code should be clean and well-documented.

Example: Suppose you need to select 6 unique numbers for a lottery ticket, 
where numbers should be in the range from 1 to 49. You can use your function like this:

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)

This code calls the get_numbers_ticket function with parameters min=1, max=49, and quantity=6. 
As a result, you will receive a list of 6 random, unique, and sorted numbers, for example, [4, 15, 23, 28, 37, 45]. 
Each time you call the function, you will get a different set of numbers.
'''

import random

def get_numbers_ticket(min_val, max_val, quantity):
    try:
        # Check if min is less than 1 or max is greater than 1000
        if min_val < 1:
            raise ValueError("Minimum value should be no less than 1.")
        if max_val > 1000:
            raise ValueError("Maximum value should be no more than 1000.")

        # Check if min is greater than max
        if min_val >= max_val:
            raise ValueError("Minimum value should be less than maximum value.")

        # Check if quantity is valid
        if quantity <= 0 or quantity > (max_val - min_val + 1):
            raise ValueError("Invalid quantity of numbers.")

        # Generate a set of unique random numbers
        numbers_set = set()
        while len(numbers_set) < quantity:
            numbers_set.add(random.randint(min_val, max_val))

        # Convert set to sorted list
        numbers_list = sorted(numbers_set)
        return numbers_list

    except ValueError as ve:
        print("Error:", ve)
        return []

# Get user input for min, max, and quantity
min_val = int(input("Enter the minimum possible number: "))
max_val = int(input("Enter the maximum possible number: "))
quantity = int(input("Enter the quantity of numbers to select: "))

# Test the function
lottery_numbers = get_numbers_ticket(min_val, max_val, quantity)
if lottery_numbers:
    print("Your lottery numbers:", lottery_numbers)
