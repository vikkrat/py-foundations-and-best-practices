from decorators.phone_number_validator import phone_number_validator
from decorators.handle_exceptions import handle_exceptions
from models.commands import Commands

# Changes an existing contact's phone number.
@handle_exceptions
@phone_number_validator(Commands.CHANGE)
def change_contact(args, contacts) -> str:
    name, new_phone = args
    contacts[name] = new_phone
    return f"Contact {name} updated to new number {new_phone}."