import os
# from note import Note
class View():

    def view_data(self, data: str, clear=False):
        if clear:
            os.system('cls')
        print('ЗАМЕТКИ:')
        if data:
            print(data)        
        else:
            print("Заметок нет")
        print()


    def view_menu(self, menu, clear=False):
        if clear:
            os.system('cls')
        print('МЕНЮ:')
        if menu:
            for punkt in menu.keys():
                print(f'{punkt}. {menu[punkt]}')
        else:
            print('В меню нет пунктов для вывода')
        print()


    def view_sub_menu(self, sub_menu, clear=False):
        if clear:
            os.system('cls')
        if sub_menu:
            for element in sub_menu:
                print(element)


    def view_data_menu(self, data, menu, clear=False):
        if clear:
            os.system('cls')
        self.view_data(data)
        self.view_menu(menu)
