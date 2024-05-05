'''
Create a Python program that calculates the area of a room by obtaining the values of length and width from the user through the input function and converting them from string type to numerical (float).

Tasks:
• Use the input function to obtain the values of room length (length) and width (width) from the user.
• Ensure that the entered data is converted from string type to the numerical type float immediately after obtaining it through input.
• Calculate the area of the room (area) by multiplying the converted values of length and width.

Expected result:
• The program should ask the user for the length and width of the room, convert these values from strings to real numbers, and then calculate the area of the room.

Tips:
• Remember that input always returns a string value, so it needs to be converted to a numerical type if you plan to use this data for mathematical calculations.
• Use float() to convert string input into a real number.
'''

# Prompt the user for the length and width of the room
length_input = input("Please enter the length of the room in meters: ")
width_input = input("Please enter the width of the room in meters: ")

# Convert the string inputs to floats
try:
    length = float(length_input)
    width = float(width_input)
except ValueError:
    print("Invalid input: Please ensure you enter numeric values.")
    length = 0
    width = 0

# Calculate the area of the room
area = length * width

# Output the result
print(f"The area of the room is {area} square meters.")

