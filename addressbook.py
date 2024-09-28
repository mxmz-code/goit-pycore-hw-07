from collections import UserDict
from record import Record
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self, days=7):
        today = datetime.now().date()
        upcoming = []
        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday.value.replace(year=today.year)
                if today <= birthday <= today + timedelta(days=days):
                    upcoming.append(record)
        return upcoming

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())
