from collections import UserDict
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Contact not found.")

    def get_upcoming_birthdays(self, days):
        now = datetime.now()
        upcoming = []
        for record in self.data.values():
            if record.birthday:
                next_birthday = record.birthday.value.replace(year=now.year)
                if now <= next_birthday <= now + timedelta(days=days):
                    upcoming.append(record)
        return "\n".join(str(record) for record in upcoming)