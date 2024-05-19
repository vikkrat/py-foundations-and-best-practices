from src.utils import handle_exceptions

# Parses the user input into a command and its arguments.
@handle_exceptions
def parse_input(user_input: str) -> (tuple[None, list] | tuple):
    parts = user_input.split()
    if not parts:
        return None, []
    cmd = parts[0].lower()
    args = parts[1:]

    return cmd, args