import view
import controller as contr

file_name = "phonebook.txt"
file = open(file_name, "a+", encoding='utf-8')


def choice_result():
    choice = contr.choice()
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        exit()
    else:
        view.error_num_comm()



def search_contact():
    search_two_name = contr.two_name()
    search_two_name = search_two_name.title()
    file1 = open(file_name, "r+", encoding='utf-8')
    file_content = file1.readlines()
    find = False
    for i in file_content:
        if search_two_name in i:
            view.contact_comp(i)
            find = True
    if not find:
        view.contact_fail(search_two_name)






def add_contact():
    first_name = contr.add_name()
    first_name = first_name.title()
    two_name = contr.two_name()
    two_name = two_name.title()
    number = contr.add_number()
    comment = contr.add_comm()
    contact = ("[" + first_name + " " + two_name + ", " + number + ", " + comment + "]\n")
    file = open(file_name, "a", encoding='utf-8')
    file.write(contact)
    view.comp_add_contact(contact)

def check_cont():
    if contr.pro_continue() == 4:
        cod_continue = True
    else:
        cod_continue = False
    return cod_continue
