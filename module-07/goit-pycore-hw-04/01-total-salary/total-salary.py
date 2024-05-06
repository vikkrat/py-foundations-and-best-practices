'''
Task 1
--------------------------------------------------------------------------------------------

You have a text file containing information about the monthly salaries of developers in your company. 
Each line in the file contains the developer's last name and their salary, separated by a comma without spaces.

For example:

• Alex Korp,3000
• Nikita Borisenko,2000
• Sitarama Raju,1000

Your task is to develop a function total_salary(path), which analyzes this file and returns the total 
and average salary of all developers.

Requirements:

• The function total_salary(path) should take one argument - the path to the text file (path).
• The file contains data about the salaries of developers, separated by commas. Each line indicates one developer.
• The function should analyze the file, calculate the total and average salary.
• The result of the function is a tuple of two numbers: the total salary and the average salary.

Recommendations for implementation:

• Use the context manager with for reading files.
• Remember to set the encoding when opening files.
• To split the data in each line, you can use the split(',') method.
• Calculate the total salary first, then divide it by the number of developers to get the average salary.
• Handle possible exceptions when working with files, such as the absence of the file.

Evaluation criteria:

• The function should accurately calculate the total and average sums.
• Handling cases where the file is missing or corrupted is necessary.
• The code should be clean, well-structured, and understandable.

Example of using the function:

total, average = total_salary("path/to/salary_file.txt")
print(f"Total salary: {total}, Average salary: {average}")

Expected result:

Total salary: 6000, Average salary: 2000
'''

import os

def total_salary(path):
    try:
        total_salary = 0
        num_developers = 0
        
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Split each line by comma and extract the salary
                _, salary_str = line.strip().split(',')
                
                # Convert salary to integer and add to total
                salary = int(salary_str)
                total_salary += salary
                
                # Increment the count of developers
                num_developers += 1
        
        # Calculate the average salary
        if num_developers > 0:
            average_salary = total_salary / num_developers
        else:
            average_salary = 0
        
        return total_salary, average_salary
    
    except FileNotFoundError:
        print("File not found.")
        return None, None
    except ValueError:
        print("Error: Invalid data format in the file.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

# Get the current directory of the script
current_directory = os.path.dirname(__file__)

# Construct the full path to the salary-info.txt
file_path = os.path.join(current_directory, "salary-info.txt")

# Test the function
total, average = total_salary(file_path)

if total is not None and average is not None:
    print(f"Total salary: {total}, Average salary: {average}")
