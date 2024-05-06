'''
Create a Python program that modifies an empty dictionary called cat by adding various keys and values to it, 
and also utilizes values from another dictionary called info.

Tasks:
• Use the dictionary cat to store information about a cat. Add the following keys and their corresponding values:
• Key "nick" with a string value representing the cat's name (for example, "Simon").
• Key "age" with an integer value representing the cat's age (for example, 7).
• Key "characteristics" with a list of the cat's characteristics (for example, ["gentle", "bites"]).
• Declare a variable age and use the get method to retrieve the cat's age from the cat dictionary.
• Use the update method to add all key-value pairs from the info dictionary to the cat dictionary.

Expected result:
• After executing the program, the cat dictionary should contain all the specified information about the cat, 
including the name, age, characteristics, and additional data from the info dictionary.
'''

# Create an empty dictionary cat
cat = {}

# Add keys and values to the cat dictionary
cat["nick"] = "Simon"
cat["age"] = 7
cat["characteristics"] = ["gentle", "bites"]

# Declare a variable age and use the get method to retrieve the cat's age
age = cat.get("age")

# Declare the info dictionary
info = {"color": "gray", "breed": "British Shorthair"}

def update_cat():
    cat.update(info)

# Call the function to update the cat dictionary
update_cat()

# Print the updated cat dictionary
print(cat)
