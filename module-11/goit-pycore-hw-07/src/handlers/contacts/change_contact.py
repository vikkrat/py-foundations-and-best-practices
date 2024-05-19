from src.utils import phone_number_validator, handle_exceptions

from src.models import Commands, AddressBook

# Changes an existing contact's phone number.
@handle_exceptions
@phone_number_validator(Commands.CHANGE)
def change_contact(args, book: AddressBook) -> str:
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return f"Contact {name} updated to new number {new_phone}."
    return "Contact not found."