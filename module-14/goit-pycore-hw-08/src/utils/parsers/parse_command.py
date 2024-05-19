from src.models import Commands

# Parsing a string input to an enum
def parse_command(command: str)-> Commands:
    return Commands[command.upper()]