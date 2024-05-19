from src.utils import phone_number_validator, handle_exceptions

from src.models import Commands, AddressBook, Record

# Adds a new contact in the dictionary.
@handle_exceptions
@phone_number_validator(Commands.ADD)
def add_contact(args, book: AddressBook) -> str:
    name, phone = args
    record = book.find(name)
    if record:
        record.add_phone(phone)
        return f"Contact {name} was updated."
    else:
        book.add_record(Record(name, [phone]))
        return f"New contact {name} added with number {phone}."