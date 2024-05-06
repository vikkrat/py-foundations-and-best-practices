from decorators.handle_exceptions import handle_exceptions
from models.errors import errors

# Shows the phone number for the specified contact.
@handle_exceptions
def show_phone(args, contacts):
    if len(args) != 1:
        return errors['show_phone_error']
    name = args[0]
    if name not in contacts:
        return errors['contact_not_found_error']
    return f"{name}: {contacts[name]}"