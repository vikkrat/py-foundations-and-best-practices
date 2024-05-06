'''
Task 4
--------------------------------------------------------------------------------------------

Write a console assistant bot that will recognize commands entered from the keyboard and 
respond according to the entered command.

☝ The assistant bot should become a prototype for the assistant application we will develop 
in the following homework assignments. Initially, the assistant application should be able 
to work with a contact book and a calendar.

In this homework, we will focus on the interface of the bot itself. The simplest and most convenient 
interface at the initial stage of development is a console application CLI (Command Line Interface). 
A CLI is fairly simple to implement.

Any CLI consists of three main elements:

• Command parser. The part that is responsible for parsing the lines entered by the user, extracting 
  keywords and command modifiers from the line.
• Command handler functions - a set of functions, also called handlers, which are responsible for 
  the direct execution of commands.
• Request-response loop. This part of the application is responsible for receiving data from the user 
  and returning the user's response from the handler function.

At the first stage, our assistant bot should be able to store a name and phone number, find a phone number by name, 
change a recorded phone number, and display all stored entries in the console. To implement such simple logic, 
we will use a dictionary. In the dictionary, we will store the user's name as a key and the phone number as a value.

Requirements for the task:

• The program must have a main() function that manages the main command processing loop.
• Implement a parse_input() function that will parse the user-entered line into a command and its arguments. 
  Commands and arguments must be recognized regardless of the case of the input.
• Your program should wait for the user to enter commands and process them using the appropriate functions. 
  If the command "exit" or "close" is entered, the program should terminate.
• Write handler functions for different commands, such as add_contact(), change_contact(), show_phone(), etc.
• Use a Python dictionary to store names and phone numbers. The name will be the key, and the phone number – the value.
• Your program should be able to identify and report incorrectly entered commands.

Execution Recommendations

First, we need to systematize the descriptions of our command formats for the console assistant bot. 
This will help us understand what functions need to be made for each command. Let's do this:

• "hello" command, for now, can be handled without a function using a simple print:Input: "hello"
  Output: "How can I help you?"
• "add [name] [phone number]" command. For this command, we will create an add_contact function:Input: "add John 1234567890"
  Output: "Contact added."
• "change [name] [new phone number]" command. For this command, we will create a change_contact function:Input: "change John 0987654321"
  Output: "Contact updated." or an error message if the name is not found
• "phone [name]" command. For this command, we will create a show_phone function:Input: "phone John"
  Output: [phone number] or an error message if the name is not found
• "all" command. For this command, we will create a show_all function:Input: "all"
  Output: all stored contacts with phone numbers
• "close" or "exit" command. Since we need to terminate the program here, we can manage without a function for these commands for now:Input: any of these words
  Output: "Good bye!" and the termination of the bot's operation

Any command that does not match the above formats will be considered incorrect, and the bot will display 
the message "Invalid command."

Let's start with a simple CLI bot version:

def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


When the program runs, it displays the message "Welcome to the assistant bot!" and enters an infinite loop, 
where it waits for a user command input while True.

If the user enters "close" or "exit", the program displays "Good bye!" and terminates. This is handled by the block of code:


if command in ["close", "exit"]:
    print("Good bye!")
    break

    
If the user enters "hello", the program displays "How can I help you?". 
If the entered command does not match any of these options, the program displays "Invalid command."

This code creates a simple interactive command line that reacts to a limited set of commands. 
We implemented a request-response loop, which will serve as an excellent basis for adding functionality 
in future homework assignments.

Now let's add a command parser. Rewrite our code as follows:


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

    
We added the parse_input(user_input) function, which takes the user input string user_input and splits it 
into words using the split() method. It returns the first word as the command cmd and the rest as a list of arguments *args. 
The line of code cmd, *args = user_input.split() splits the string into words. The first word is stored in the variable cmd, 
and the rest is stored in the list args thanks to the unpacking operator *. Then, the line of code cmd = cmd.strip().lower() 
emoves any extra spaces around the command and converts it to lowercase.

☝ Why convert the command to lowercase?

Suppose a user enters the command as "HELLO", "Hello", or "hello". 
If you do not convert these variants to a common register, they will be considered different commands, 
and you will have to handle each variant separately.

Converting the command to lowercase allows you to avoid this by transforming all variants into the same form. 
This way, you can easily compare the entered command with predefined commands regardless of how the user entered it.
This provides a better user experience, as the program becomes less sensitive to the specific way commands are entered.

The result in the main function we get after executing the line of code command, *args = parse_input(user_input).

The parse_input function splits the entered string into words using a space as a delimiter. 
The variable command receives the first value and is considered a command, 
and the variable args becomes a list of all other values.

For example, if we enter the command "add John 123456", the variable command will become the string "add", 
and the variable args will become the list ["John", "123456"]. If we enter the command "hello", 
then command will be the string "hello", and args will be an empty list [].

We hope you now understand the principle of the parser; it's time to add the add command.

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

    
We added a dictionary of contacts contacts = {} inside the main function and a handler function for the add_contact command.

The add_contact function is designed to add a new contact to the contact dictionary. 
It takes two arguments: args, which is a list containing the name and phone number, 
and contacts, which is a dictionary where contacts are stored.

Inside the function, the two elements from the args list are unpacked into the variables name and phone. 
The function then adds a "key: value" pair to the contact dictionary, using the name as the key and the phone number 
as the value contacts[name] = phone.

☝ It should be noted that if a contact with such a name already exists, its data will be overwritten without any warnings. 
Here you can act at your discretion, whether you want to handle the collision or not, in our version we overwrite the contact.

The add_contact function returns a string confirming the successful addition of the contact: "Contact added.".

It is necessary to note that this function does not have built-in error checks. For example, 
if args does not contain two elements, this function will cause a ValueError.

ValueError: not enough values to unpack (expected 2, got 0)

Leave error handling at your discretion in this homework assignment, as we will add error handling through decorators 
in the next homework assignment.

Evaluation Criteria:

• The bot must remain in an infinite loop, waiting for the user's command.
• The bot terminates its work if it encounters the words: "close" or "exit".
• The bot is not sensitive to the case of the entered commands.
• The bot accepts commands:
  1. "hello", and responds in the console with the message "How can I help you?"
  2. "add username phone". For this command, the bot stores a new contact in memory, for example in a dictionary. 
      The user enters the name username and the phone number phone, necessarily separated by a space.
  3. "change username phone". For this command, the bot stores a new phone number phone for the existing contact username 
      in the notebook.
  4. "phone username" For this command, the bot displays the phone number for the specified contact username in the console.
  5. "all". For this command, the bot displays all stored contacts with phone numbers in the console.
  6. "close", "exit" for any of these commands, the bot ends its work after displaying the message "Good bye!" 
      in the console and terminating its execution.
• The logic of the commands is implemented in separate functions, and these functions take one or more lines as input and return a line.
• All user interaction logic is implemented in the main function, all prints and inputs occur only there.
'''

from parsers.parse_input import parse_input
from parsers.parse_command import parse_command
from decorators.handle_exceptions import handle_exceptions

from models.commands import Commands
from models.messages import messages
from models.errors import errors

from handlers import *

# The main function that drives the assistant bot.
@handle_exceptions
def main():
    contacts = {}
    print(messages['welcome'])

    while True:
        user_input = input(messages['enter_command'])
        command, args = parse_input(user_input)
        parsed_command = parse_command(command)

        match parsed_command:
            case Commands.CLOSE | Commands.EXIT:
                complete_session()
                break
            case Commands.HELLO:
                start_session()
            case Commands.ADD:
                print(add_contact(args, contacts))
            case Commands.CHANGE:
                print(change_contact(args, contacts))
            case Commands.PHONE:
                print(show_phone(args, contacts))
            case Commands.ALL:
                print(show_all(contacts))
            case _:
                print(errors['key_error'])

        
if __name__ == "__main__":
    main()
