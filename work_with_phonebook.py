from show_menu import*
from read_txt import*
from print_result import*
from find_contact import*
from get_new_number import*
def work_with_phonebook():

    choice=show_menu() # перейти в шоуменю

    phone_book=read_txt('phonebook.txt') # перейти в реадтхт

    while (choice!=5):

        if choice==1:
            print_result(phone_book) # перейти в принттхт/выводим справочник
            break
        elif choice==2:
            print(find_contact(phone_book)) # перейти в файндконтакт по имени и фамилии
            break
        elif choice==3:
            print(add_phone_number('phonebook.txt')) # добавить
            break
        elif choice==4:
            print('До свидания!')
            break
    else:
        print('Неправильно выбрана команда!')