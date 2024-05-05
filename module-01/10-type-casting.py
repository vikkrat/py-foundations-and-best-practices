'''
Create a Python program that asks the user for personal information and stores it in corresponding variables.

Tasks:
• Use the input function to obtain the following data from the user:

• name, as a string.
• email, as a string.
• age, as an integer, type int.
• height, as a real number, type float.
• is_active, as a boolean value, indicating the desire to receive messages from the site.

• Create a separate question for each variable according to its data type.
• Ensure that the entered data is converted to the correct data type before being saved in the variables.

Expected result:
• The program should ask the user for their name, email, age, height, and whether they wish to receive messages, and store this information in the corresponding variables.

Tips:
• Use int() and float() to convert string values to the appropriate numerical types.
• To convert string input into a boolean value, assume that if the user does not agree, they enter nothing into the input function.
'''

# Prompt for the user's name
name = input("Please enter your name: ")

# Prompt for the user's email
email = input("Please enter your email: ")

# Prompt for the user's age and convert the input to an integer
try:
    age = int(input("Please enter your age: "))
except ValueError:
    age = None  # Handles case where input is not a valid integer

# Prompt for the user's height and convert the input to a float
try:
    height = float(input("Please enter your height in meters: "))
except ValueError:
    height = None  # Handles case where input is not a valid float

# Prompt for the user's preference on receiving messages from the site
is_active_input = input("Do you wish to receive messages from our site? (yes/no): ")
is_active = True if is_active_input.lower() == 'yes' else False

# Print the collected data
print("\nCollected User Information:")
print(f"Name: {name}")
print(f"Email: {email}")
print(f"Age: {age}")
print(f"Height: {height} meters")
print(f"Active user (receiving messages): {is_active}")
