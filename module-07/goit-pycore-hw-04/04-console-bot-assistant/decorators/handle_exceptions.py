import functools
from models.errors import errors

def handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print(errors['key_error'])
        except ValueError:
            print(errors['value_error'])
        except Exception as e:
            # Log the exception or handle it as needed
            print(f"{errors['exception']} {str(e)}")
            # Optionally, return a default value or re-raise the exception
            return errors['something_went_wrong']
    return wrapper
