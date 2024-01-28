from read_txt import*

def print_result(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()
phone_book=read_txt('phonebook.txt')