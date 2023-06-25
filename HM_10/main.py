from collections import UserDict


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
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phones = []
        self.add_phone(phone)

    @input_error
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    @input_error
    def change_phone(self, new_phone):
        for phone in self.phones:
            phone.value = new_phone

    def show_phones(self):
        return [phone.value for phone in self.phones]


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


def main():
    address_book = AddressBook()
    print("Bot started, please enter your command")
    while True:
        command = input("Enter command:>>>")
        if command == 'hello':
            print('How can I help you?')
        elif command.startswith('add'):
            _, name, phone = command.split(' ')
            if name not in address_book.data:
                record = Record(name, phone)
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
        elif command == 'good bye' or command == 'close' or command == 'exit':
            print('Bye')
            break
        else:
            print('Unknown command. Please try again.')


if __name__ == '__main__':
    main()
