
menu_punkts=['Добавить заметку', 'Сортировать заметки', 'Фильтровать по текущей дате', 'Удалить заметку','Выйти из программы']
menu_flags =[False,False,False,False,False]

def make_menu(data):
    global menu_flags
    if data:
        menu_flags = [True,True,True,True,True]
    else:
        menu_flags =[True,False,False,False,True] 

def get_menu():
    l_flags_punkts=list(zip(menu_flags,menu_punkts))
    menu = dict(enumerate([item[1] for item in l_flags_punkts if item[0]], start=1))
    return menu

def set_menu(add=False,sort=False,filter=False,delete=False,exit=True):
    global menu_flags
    menu_flags =[add,sort,filter,delete,exit]