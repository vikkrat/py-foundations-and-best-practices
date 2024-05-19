from src.models import AddressBook

def upcoming_birthdays(args, book: AddressBook):
    days = int(args[0]) if args else 7
    return book.get_upcoming_birthdays(days)