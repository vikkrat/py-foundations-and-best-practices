import re
import functools

from src.models import Commands
from src.models import errors

# Decorator that checks if the phone number argument is valid.
def phone_number_validator(command: Commands):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Unpack arguments assuming args[0] is the list of parameters and args[1] is the contacts dictionary
            parameters, contacts = args
            if len(parameters) != 2:
                return get_command_error(command)
            
            name, phone = parameters
            
            if command == Commands.CHANGE and name not in contacts:
                return errors['contact_not_found_error']
            
            if not is_valid_phone(phone):
                return errors['phone_format_error']
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Validate a phone number based on a pattern.
def is_valid_phone(phone_number):
    pattern = r'^\+?\d{10,15}$'
    return re.match(pattern, phone_number) is not None

# Define the function that retrieves an error message based on the command type.
def get_command_error(command: Commands):
    match command:
            case Commands.CHANGE:
                return errors['change_contact_error']
            case _:
                return errors['add_contact_error']
