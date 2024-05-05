'''
Create a Python program that calculates the cost of electricity consumption based on a given tariff and meter readings.

Tasks:
In the variable rate, store the cost of one kilowatt of electricity. Set this variable to 1.68.
In the variable value, store the reading of the electricity meter in kilowatts. Set value to a reasonable whole number.
Calculate the cost of electricity consumption by multiplying rate by value, and save the result in the variable payment.
'''

# Initialize the variable 'rate' with the cost per kilowatt-hour
rate = 1.68

# Initialize the variable 'value' with the electricity meter reading in kilowatts
value = 300

# Calculate the total electricity consumption cost
payment = rate * value

# Print the total cost of electricity consumption
print(f"The total cost of electricity consumption is: {payment} UAH")
