from src.utils import handle_exceptions
from src.models import errors, AddressBook

# Shows the phone number for the specified contact.
@handle_exceptions
def show_phone(args, book: AddressBook):
    if len(args) != 1:
        return errors['show_phone_error']
    name = args[0]
    record = book.find(name)
    if record:
        return f"{name}: {', '.join(phone.value for phone in record.phones)}"
    return errors['contact_not_found_error']