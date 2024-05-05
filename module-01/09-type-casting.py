'''
Let's return to the task of calculating the area. Create a Python program that calculates the area of a room by converting the string values of length and width into numbers, and forms an informative message about the result.

Tasks:
• Declare the variables length and width with string values for the room's length and width. Set them to "2.75" and "1.75".
• Convert the string values of length and width to real numbers (type float) when calculating the area.
• Calculate the area of the room, area, as the product of the converted values of length and width.
• Create a variable show that will contain an informative string with the template: 'With width <width value> and length <length value> of the room, its area is equal to <area value>'.

Expected result:
The program should save in the variable show an informative string about the dimensions of the room 
and its area, using the conversion from string to numerical values of length and width.

Tips:
• Use the float() function to convert string values into real numbers.
• In the variable show, ensure that the correct dimensions and area of the room are displayed.
'''

# Declare variables for length and width with string values
length = "2.75"
width = "1.75"

# Convert string values to floats for calculation
length_float = float(length)
width_float = float(width)

# Calculate the area of the room
area = length_float * width_float

# Create an informative message using the calculated area
show = f"With width {width} and length {length} of the room, its area is equal to {area:.2f} square meters."

# Print the informative message
print(show)
