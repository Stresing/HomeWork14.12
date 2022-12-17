def show_main_menu():
    print("\n" "Введите 1 для добавление в книгу")
    print("Введите 2 для поиска в книге")
    print("Для закрытия локального меню нажмите: 3 ")


def contact_comp(name, ):
    print(f"Ваш контакт найден: ")
    print(name)


def contact_fail(fail_name):
    print("Записей: " + fail_name + "  нету в книге")


def error_num_comm():
    print("Нужно ввести 1 или 2!\n")


def comp_add_contact(con):
    print("\n" "Контакт добавлен" "\n" + con)
