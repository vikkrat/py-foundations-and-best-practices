'''
Create a Python program that initializes an empty dictionary and populates it with specific keys and corresponding values.

Tasks:
• Create an empty dictionary named data.
• Add the following key-value pairs to the dictionary data:
• Key year with the value of an integer 2024.
• Key lang with the value of a string 'Python'.
• Key version with the value of a real number 3.12.

Expected result:
• After executing the program, the dictionary data should contain the three key-value pairs as specified above.
'''

# Create an empty dictionary
data = {}

# Add key-value pairs to the dictionary
data['year'] = int(2024)          # Key 'year' with an integer value
data['lang'] = str('Python')      # Key 'lang' with a string value
data['version'] = float(3.12)       # Key 'version' with a real number value

# Print the dictionary to show the final contents
print("Contents of dictionary 'data':", data)
