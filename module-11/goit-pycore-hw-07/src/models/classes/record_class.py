from .name_class import Name
from .phone_class import Phone
from .birthday_class import Birthday

class Record:
    def __init__(self, name, phones=None, birthday=None):
        self.name = Name(name)
        self.phones = [Phone(phone) for phone in phones] if phones else []
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        raise ValueError("Old phone number not found.")

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones = ', '.join(phone.value for phone in self.phones)
        return f"Name: {self.name.value}, Phones: {phones}, Birthday: {self.birthday.value.strftime('%d.%m.%Y') if self.birthday else 'N/A'}"