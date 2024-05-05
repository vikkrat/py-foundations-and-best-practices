'''
Create a Python program that initializes an empty list and populates it with specific values at specified indices.

Tasks:
• Create an empty list called my_list.
• Add the following elements to my_list using indices for their placement:
• Place the integer 2024 at the position with index 0.
• Place the string 'Python' at the position with index 1.
• Place the real number 3.12 at the position with index 2.

Expected result:
• After executing the program, the list my_list should contain three elements in the specified order: an integer, a string, and a real number.

Tips:
• You can use the insert() method to add elements to the list at the respective positions.
• Ensure that the elements are added in the correct order according to the specified indices.
'''

# Create an empty list
my_list = []

# Use the insert method to add elements at specific indices
my_list.insert(0, int(2024))   # Insert integer 2024 at index 0
my_list.insert(1, 'Python')  # Insert string 'Python' at index 1
my_list.insert(2, float(3.12))    # Insert real number 3.12 at index 2

# Print the list to verify the contents
print("Contents of my_list:", my_list)
