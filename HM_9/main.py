contacts = {}


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


@input_error
def add_phone(command):
    _, name, phone = command.split(' ')
    contacts[name] = phone
    print('Контакт додано: {} - {}'.format(name, phone))


@input_error
def phone_change(command):
    _, name, phone = command.split(' ')
    if name in contacts:
        contacts[name] = phone
        return 'Phone number updated for contact {}: {}'.format(name, phone)
    else:
        return 'Contact {} not found'.format(name)


# @input_error
def show_phone(command):
    _,name = command.split(' ', 1)
    if name in contacts:
        return 'Phone numbre for {}:{}'.format(name, contacts[name])
    else:
        return 'Contact {} not found'.format(name)


def main():
    print('Bot started. Enter your commands.')
    while True:
        command = input('Enter the command> ').lower()
        if command == 'hello':
            print('How can I help you?')
        elif command.startswith('add'):
            add_phone(command)
        elif command.startswith('change'):
            print(phone_change(command))
        elif command.startswith('phone'):
            print(show_phone(command))
        elif command == 'show all':
            print(contacts)
        elif command == 'good bye' or command == 'close' or command == 'exit':
            print('bye')
            break
        else:
            print('Unknown command. Please try again.')


if __name__ == '__main__':
    main()
