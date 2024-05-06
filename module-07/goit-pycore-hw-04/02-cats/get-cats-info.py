'''
Task 2
--------------------------------------------------------------------------------------------

You have a text file containing information about cats. Each line of the file contains a unique identifier 
for the cat, its name, and age, separated by commas. For example:

• 60b90c1c13067a15887e1ae1,Tayson,3
• 60b90c2413067a15887e1ae2,Vika,1
• 60b90c2e13067a15887e1ae3,Barsik,2
• 60b90c3b13067a15887e1ae4,Simon,12
• 60b90c4613067a15887e1ae5,Tessi,5

Your task is to develop a function get_cats_info(path) that reads this file and returns a list of dictionaries 
with information about each cat.

Requirements:

• The get_cats_info(path) function should take one argument - the path to the text file (path).
• The file contains data about cats, where each record contains a unique identifier, the cat's name, and its age.
• The function should return a list of dictionaries, where each dictionary contains information about one cat.

Recommendations for implementation:

• Use with for safe file reading.
• Remember to set the encoding when opening files.
• For each line in the file, use split(',') to obtain the identifier, name, and age of the cat.
• Create a dictionary with keys "id", "name", "age" for each cat and add it to the list to be returned.
• Handle possible exceptions related to reading the file.

Evaluation criteria:

• The function should accurately process the data and return the correct list of dictionaries.
• Proper handling of exceptions and errors is required.
• The code should be clean, well-structured, and understandable.

Example of using the function:

cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)

Expected result:

[
   {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
   {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
   {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
   {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
   {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
'''
import os

def get_cats_info(path: str) -> list:
    cats = []  # List to store cat information
    try:
        with open(path, 'r', encoding='utf-8') as file:  # Open the file with UTF-8 encoding
            for line in file:
                if line.strip():  # Ensure the line is not empty
                    id, name, age = line.strip().split(',')
                    # Create a dictionary with the cat's data
                    cat_dict: dict[str, str] = {"id": id, "name": name, "age": age}
                    cats.append(cat_dict)  # Add the dictionary to the list
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return cats  # Return the list of dictionaries

# Get the current directory of the script
current_directory: str = os.path.dirname(__file__)

# Construct the full path to the cats-info.txt
file_path: str = os.path.join(current_directory, "cats-info.txt")

# Test the function
cats_info = get_cats_info(file_path)

print(cats_info)
