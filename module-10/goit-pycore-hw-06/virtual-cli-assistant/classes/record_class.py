from .name_class import Name
from .phone_class import Phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                self.phones.remove(ph)
                return True
        return False

    def edit_phone(self, old_phone, new_phone):
        for ph in self.phones:
            if ph.value == old_phone:
                ph.value = new_phone if Phone.validate(new_phone) else old_phone
                return True
        return False

    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"