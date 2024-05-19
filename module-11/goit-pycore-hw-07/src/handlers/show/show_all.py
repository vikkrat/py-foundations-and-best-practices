from src.utils import handle_exceptions
from src.models import errors, AddressBook

# Displays all contacts and their phone numbers.
@handle_exceptions
def show_all(book: AddressBook) -> str:
    if not len(book.values()):
        return errors['no_contacts_saved']
    
    return "\n".join(str(record) for record in book.values())

