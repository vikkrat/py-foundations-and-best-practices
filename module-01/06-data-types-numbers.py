'''
Create a Python program that calculates the area of a room using the given length and width, and generates an informative message about the calculation results.

Tasks:
Use the variables length and width to store the length and width of the room, respectively. Set them to 2.75 and 1.75.
Calculate the area of the room area by multiplying length and width.
Create a variable show that will contain a string with information about the length, width, and area of the room. Use the string formatting function to insert the values of the variables length, width, and area into the specified template.
Template: 'With width <width value> and length <length value> of the room, its area is equal to <area value>'
Expected result:
The program should store in the variable show a string that informs about the length and width of the room and its total area.

Tips:
Use an f-string to format the show variable string, which will allow you to insert the values of the variables directly into the text.
Make sure that the length, width, and area of the room are correctly stated in the output string.
'''

# Define the length and width of the room
length = 2.75  # in meters
width = 1.75   # in meters

# Calculate the area of the room
area = length * width

# Create a message using string formatting to show the dimensions and area
show = f"With width {width} and length {length} of the room, its area is equal to {area} square meters."

# Print the informative message
print(show)