"""
Task 2

Extend Phonebook application

Functionality of Phonebook application:

Add new entries 
Search by first name 
Search by last name 
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program


The first argument to the application should be the name of the phonebook. Application should load JSON data, if it is
present in the folder with application, else raise an error. After the user exits, all data should be saved to loaded
JSON.
"""
from pprint import pprint

contacts = []
INPUT_OPTIONS = ('1', '2', '3', '4', '0')
NAVIGATION = '1 - create a new entire\n' \
             '2 - update an entire\n' \
             '3 - remove an entire\n' \
             '4 - search an entire\n' \
             '5 - show contact list\n' \
             '0 - exit'


def create_new_contact():
    phone = input('Enter phone number:\n')
    first_name = input('Enter first name:\n')
    last_name = input('Enter last name:\n')
    city = input('Enter city:\n')

    contact = {
        phone: {
            'first_name': first_name,
            'last_name': last_name,
            'full_name': f'{first_name} {last_name}',
            'city': city,
        }
    }

    contacts.append(contact)


def remove_contact():
    phone = input('Enter phone number that you want to delete:\n')
    for c in contacts:
        if c[phone]:
            contacts.remove(c)
    print(phone, 'was deleted.')


def search_contact():
    user_input = input('Enter phone num to search?\n')

    for entire in contacts:
        if user_input in entire:
            pprint(entire)
        else:
            print('There is not such contact in phonebook.')


def communicator():
    while True:
        user_input = input('>>> ')
        if user_input not in INPUT_OPTIONS:
            print('Invalid input. Try again.')
            continue
        else:
            return user_input


def phonebook():
    print(NAVIGATION)

    while True:
        user_input = communicator()

        if user_input == '1':
            create_new_contact()
        elif user_input == '2':
            remove_contact()
        elif user_input == '3':
            search_contact()
        elif user_input == '4':
            pprint(contacts)
        elif user_input == '0':
            break


if __name__ == '__main__':
    phonebook()
