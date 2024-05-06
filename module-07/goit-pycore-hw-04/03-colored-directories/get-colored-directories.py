'''
Task 3
--------------------------------------------------------------------------------------------

Develop a script that takes a directory path as a command-line argument and visualizes the structure 
of that directory, displaying the names of all subdirectories and files. For better visual perception, 
the names of directories and files should be differentiated by color.

Task Requirements:

• Create a Python virtual environment to isolate project dependencies.
• The script must receive the directory path as a launch argument. This path indicates where the directory 
  is located, the structure of which needs to be displayed.
• Use the colorama library for implementing colored output.
• The script should correctly display both the names of directories and files, using a recursive approach 
  to traverse directories (optionally, a non-recursive approach may be used).
• There must be error checking and handling, for example, if the specified path does not exist or does not 
  lead to a directory.

Recommendations for Implementation:

• First, install the colorama library. Do this by creating and activating a Python virtual environment, 
  then install the package using pip.
• Use the sys module to obtain the directory path as a command-line argument.
• Use the pathlib module to work with the file system.
• Ensure proper output formatting using the colorama functions.

Evaluation Criteria:

• Creation and use of a virtual environment.
• Correctness in obtaining and processing the directory path.
• Accuracy in displaying the directory structure.
• Proper application of colored output using colorama.
• Code quality, including readability, structuring, and comments.

Example Usage:

If you execute the script and pass it the absolute path to the directory as a parameter:

python hw03.py /path/to/your/directory

This will result in the terminal displaying a list of all subdirectories and files in the specified directory 
using different colors for subdirectories and files, which facilitates visual perception of the file structure.

For a directory with the following structure:

📦picture
 ┣ 📂Logo
 ┃ ┣ 📜IBM+Logo.png
 ┃ ┣ 📜ibm.svg
 ┃ ┗ 📜logo-tm.png
 ┣ 📜bot-icon.png
 ┗ 📜mongodb.jpg

The script should display a similar structure.
'''

import sys
from pathlib import Path
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def get_colored_directories(path, level=0):
    try:
        base_path = Path(path)

        if not base_path.exists():
            print(f"{Fore.RED}Error: The path {path} does not exist.")
            return
        
        if not base_path.is_dir():
            print(f"{Fore.RED}Error: The path {path} is not a directory.")
            return

        for item in base_path.iterdir():
            prefix = " " * (level * 4)
            if item.is_dir():
                print(f"{prefix}{Fore.BLUE}{item.name}/")
                get_colored_directories(item, level + 1)
            else:
                print(f"{prefix}{Fore.GREEN}{item.name}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python {sys.argv[0]} <directory_path>")
    else:
        directory_path = sys.argv[1]
        get_colored_directories(directory_path)


