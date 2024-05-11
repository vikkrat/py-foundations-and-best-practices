from decorators.handle_exceptions import handle_exceptions
from models.errors import errors

# Displays all contacts and their phone numbers.
@handle_exceptions
def show_all(contacts) -> str:
    if not contacts:
        return errors['no_contacts_saved']
    
    return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())