from enum import Enum, auto

# This enum holds exeptable for bot-assistant commands.
class Commands(Enum):
    HELLO = auto()
    ADD = auto()
    CHANGE = auto()
    PHONE = auto()
    ALL = auto()
    CLOSE = auto()
    EXIT = auto()
    ADD_BIRTHDAY = auto()
    SHOW_BIRTHDAY = auto()
    BIRTHDAYS = auto()