from src.models import AddressBook

def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return record.birthday.value.strftime('%d.%m.%Y')
    return "Birthday not found."