from collections import UserDict
from datetime import datetime, date, timedelta


def input_error(handler_func):
    def wrapper(*args, **kwargs):
        try:
            return handler_func(*args, **kwargs)
        except KeyError:
            print('Enter user name')
        except ValueError:
            print('Give me name and phone please')
        except IndexError:
            print('Invalid input, please try again')
    return wrapper


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.current_page = 1
        self.page_size = 5

    def add_record(self, record):
        self.data[record.name.value] = record

    def iterator(self):
        total_records = len(self.data)
        total_pages = (total_records - 1) // self.page_size + 1
        start_index = (self.current_page - 1) * self.page_size
        end_index = self.current_page * self.page_size
        records = list(self.data.values())[start_index:end_index]
        for record in records:
            yield record

        print(f"Page {self.current_page} of {total_pages}")
        print(f"Total records: {total_records}")
        print()

    def next_page(self):
        total_pages = (len(self.data) - 1) // self.page_size + 1
        if self.current_page < total_pages:
            self.current_page += 1
            self.show_current_page()
        else:
            print("No more pages available")

    def previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.show_current_page()
        else:
            print("Already at the first page")

    def show_current_page(self):
        print(f"--- Page {self.current_page} ---")
        for record in self.iterator():
            print(record)
            print()

        print(f"--- Page {self.current_page} ---")
        print()

    def show_all(self):
        print("All records:")
        for record in self.data.values():
            print(record)
            print()


class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.add_phone(phone)
        self.birthday = None
        if birthday:
            self.birthday = Birthday(birthday)

    def add_birthday(self, birthday):
        if self.birthday:
            print('Contact already has a birthday')
        else:
            self.birthday = Birthday(birthday)
            print('Birthday added for contact', self.name.value)

    @input_error
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    @input_error
    def change_phone(self, new_phone):
        for phone in self.phones:
            phone.value = new_phone

    def days_to_birthday(self, birthday):
        today = date.today()
        birthday = datetime.strptime(birthday, "%d.%m.%Y").date()

        next_birthday = date(today.year, birthday.month, birthday.day)

        if next_birthday < today:
            next_birthday = date(today.year + 1, birthday.month, birthday.day)

        days_left = (next_birthday - today).days
        return days_left

    def show_phones(self):
        return [phone.value for phone in self.phones]


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(None)
        self.value = self.validate(value)

    @staticmethod
    def validate(value):
        if not value.startswith("+"):
            raise ValueError(
                "Invalid phone number format. Phone number must start with '+'")
        return value


class Birthday(Field):
    def __init__(self, value):
        super().__init__(None)
        self.value = self.validate(value)

    @staticmethod
    def validate(value):
        try:
            date_format = "%d-%m-%Y"
            parsed_date = datetime.strptime(value, date_format)
            return parsed_date.date()
        except ValueError:
            raise ValueError(
                "Invalid birthday format. Birthday must be in the format 'DD-MM-YYYY'")


def main():
    address_book = AddressBook()
    print("Bot started, please enter your command")
    while True:
        command = input("Enter command:>>>")
        if command == 'hello':
            print('How can I help you?')
        elif command.startswith('add'):
            _, name, phone, *birthday = command.split(' ')
            if name not in address_book.data:
                record = Record(name, phone, birthday[0] if birthday else None)
                address_book.add_record(record)
                print('Contact added: {} - {}'.format(name, phone))
            else:
                print('Contact already exists')
        elif command.startswith('change'):
            _, name, new_phone = command.split(' ')
            if name in address_book.data:
                record = address_book.data[name]
                record.change_phone(new_phone)
                print('Phone changed to {} for contact {}'.format(new_phone, name))
            else:
                print('Contact not found')
        elif command == 'show all':
            for name, record in address_book.data.items():
                print('Name: {}'.format(name))
                print('Phones: {}'.format(', '.join(record.show_phones())))
                print()
        elif command.startswith('phone'):
            _, name = command.split()
            if name in address_book.data:
                record = address_book.data[name]
                print('Phone number for {}: {}'.format(
                    name, ', '.join(record.show_phones())))
            else:
                print("Contact not found")
        elif command == 'next':
            address_book.next_page()
        elif command == 'prev':
            address_book.previous_page()
        elif command.startswith('birth_add'):
            _, name, birthday = command.split(' ')
            if name in address_book.data:
                record = Record(name, birthday)
                address_book.add_record(record)
                print("date of birth added to {} and is {}".format(name, birthday))
        elif command == 'good bye' or command == 'close' or command == 'exit':
            print('Bye')
            break
        else:
            print('Unknown command. Please try again.')


if __name__ == '__main__':
    main()
