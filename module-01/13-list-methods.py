'''
Create a Python program that performs a series of operations with two lists, changing their content and the order of elements.

Tasks:
• Having two lists, my_list and some_data, use the extend method to add all elements from some_data to the end of my_list.
• Use the insert method to add the string 'Python' at the position with index 1 in my_list.
• Use the reverse method to reverse the order of elements in my_list.

Expected result:
• After executing the program, the list my_list should reflect the specified changes.
'''

# Define two lists
my_list = [10, 20, 30]
some_data = [40, 50, 60]

# Use the extend method to add all elements from some_data to the end of my_list
my_list.extend(some_data)

# Use the insert method to add 'Python' at index 1
my_list.insert(1, 'Python')

# Use the reverse method to reverse the order of elements in my_list
my_list.reverse()

# Print the modified list to show the final state
print("Modified my_list:", my_list)
