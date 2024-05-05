'''
The Boolean type is often used to indicate the state of an object. 
For example, the variable is_active can indicate whether a user's account is active or not. 
Also, user accounts are often not deleted from the database but are simply set with the property is_delete – 
this is called a soft delete. Using the Boolean data type in Python, 
set the state of user accounts with the variables is_active and is_delete.

Tasks:
Set the variable is_active to True to indicate that the user's account is active.
Set the variable is_delete to False to indicate that the user's account is not deleted.
Expected result: After running the program, you should have two Boolean variables: 
is_active with a true value and is_delete with a false value.
'''

# Set the variable is_active to True indicating the user's account is active
is_active = True

# Set the variable is_delete to False indicating the user's account is not deleted
is_delete = False

# Print the values of is_active and is_delete to verify their states
print("Account Active:", is_active)
print("Account Deleted:", is_delete)