from src.utils import *
from src.handlers import *
from src.models import *


# The main function that drives the assistant bot.
@handle_exceptions
def main():
    book = load_data()
    print(messages['welcome'])

    while True:
        user_input = input(messages['enter_command'])
        command, args = parse_input(user_input)
        parsed_command = parse_command(command)

        match parsed_command:
            case Commands.CLOSE | Commands.EXIT:
                save_data(book)
                complete_session()
                break
            case Commands.HELLO:
                start_session()
            case Commands.ADD:
                print(add_contact(args, book))
            case Commands.CHANGE:
                print(change_contact(args, book))
            case Commands.PHONE:
                print(show_phone(args, book))
            case Commands.ALL:
                print(show_all(book))
            case Commands.ADD_BIRTHDAY:
                print(add_birthday(args, book))
            case Commands.SHOW_BIRTHDAY:
                print(show_birthday(args, book))
            case Commands.BIRTHDAYS:
                print(upcoming_birthdays(args, book))
            case _:
                print(errors['key_error'])

        
if __name__ == "__main__":
    main()
