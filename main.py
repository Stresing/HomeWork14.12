import view
import model


def start():
    view.show_main_menu()
    model.choice_result()


start()
while model.check_cont():
    start()
else:
    exit()
