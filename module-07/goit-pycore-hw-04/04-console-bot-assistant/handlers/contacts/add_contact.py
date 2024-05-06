from decorators.phone_number_validator import phone_number_validator
from decorators.handle_exceptions import handle_exceptions
from models.commands import Commands

# Adds a new contact in the dictionary.
@handle_exceptions
@phone_number_validator(Commands.ADD)
def add_contact(args, contacts) -> str:
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added with number {phone}."