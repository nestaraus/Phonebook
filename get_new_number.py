def get_new_number():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    dop_info = input('Введите дополнительную информацию: ')
    return last_name, first_name, phone_number, dop_info 


def add_phone_number(file_name):
    info = ' , '.join(get_new_number())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')