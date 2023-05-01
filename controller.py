from notes import Notes
import model_menu as mm
import model_sub_menu as msm
from view import View
from datetime import datetime


class Controller():
    data:str
    menu:mm

    sort_id=False
    sort_header=False

    def __init__(self,model:Notes,view:View):
        self.model = model
        self.view = view
    
    def insert_record(self):
        self.view.view_data(self.data,clear=True)
        ids = []
        ids = self.model.get_ids()
        while True:
            id = -1
            s_id = input('Введите id(число) новой записи (или введите 0 для автоматического назначения id): ').strip()
            if s_id.isdigit():
                id = int(s_id)
            if id<0:
                print(f'{s_id} - недопустимо для id. Введите допустимый.')      
            elif id in ids:
                self.view.view_data(self.data,clear=True)
                print(f'{s_id} - Такой id уже существует. Введите уникальный.')
            else:
                break
        if id == 0:
            if self.data:
                id = max(ids)+1
            else:
                id = 1
            print(f'Автоматически назначен id = {id}')
        msm.clear()
        msm.add(f'Cоздание новой записи с id: {id}')
        self.view.view_sub_menu(msm.get())
        while True:
            s_name = input('Введите заголовок заметки: ').strip()
            if s_name:
                if not ';' in s_name:
                    break
            self.view.view_data(self.data,clear=True)
            self.view.view_sub_menu(msm.get())
            print(f'{s_name} - не подходит, нельзя использовать ;')
        msm.add(f'Заголовок: {s_name}')
        self.view.view_data(self.data,clear=True)
        self.view.view_sub_menu(msm.get())
        s_note = input('Введите текст заметки: ').strip()
        self.model.add(id,datetime.now(),s_name,s_note)

    def delete_record(self):
        self.view.view_data(self.data,clear=True)
        while True:
            id=-2
            s_id = input('Введите id(число) записи, которую хотите удалить, -1 удалить все записи (или введите 0 для выхода из меню.): ').strip()
            if s_id.isdigit():
                id = int(s_id)
            if id in self.model.get_ids() or id == 0 or s_id == '-1':
                break
            else:
                self.view.view_data(self.data,clear=True)
                print(f'{s_id} - такого id нет или некорректный ввод. Введите существующий.')
        if s_id == '-1':
            self.model.remove_all()
        elif id != 0:
            self.model.remove(id)
        
    def sort_record(self):
        self.view.view_data(self.data,clear=True)
        while True:
            s_id = input('Выберите: 1 - сортировать записи по id, 2 - сортировать по заголовку, 0 - не менять сортировать: ')
            if s_id.isdigit():
                id = int(s_id)
            if 2 >= id >= 0:
                break
            else:
                self.view.view_data(self.data,clear=True)
                print(f'{s_id} - такого пункта нет. Введите существующий.')
        if id == 0:
            pass
        elif id == 1:
            self.model.sort_id()
        else:
            self.model.sort_header()
        
    def filter_date(self):
        self.view.view_data(self.model.get_today(),clear=True)
        __ = input('Нажмите Enter для того, чтобы продолжить')





    def choice(self):
    
        punkt_id = 0
        while True:
            s_punkt_id = input('Введите номер меню: ')
            if s_punkt_id.isdigit():
                punkt_id = int(s_punkt_id)
            if punkt_id in self.menu:
                break
            else:
                self.view.view_data_menu(self.data,self.menu,clear=True)
                print(f'{s_punkt_id} - неправильный выбор')
        match self.menu[punkt_id]:
            case 'Добавить заметку':
                self.insert_record()
            case 'Удалить заметку':
                self.delete_record()
            case 'Сортировать заметки':
                self.sort_record()
            case 'Фильтровать по текущей дате':
                self.filter_date()
            case _:
                print('Выход из программы')
                exit()
        

    def change(self):
        self.data = self.model.get_all()
        mm.make_menu(self.data)
        self.menu=mm.get_menu()


    def start(self):

        self.change()
        self.view.view_data_menu(self.data,self.menu,clear=True)
        while True:
            self.choice()
            self.change()
            self.view.view_data_menu(self.data,self.menu,clear=True)

        
        
        
            

