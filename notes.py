from datetime import datetime
from note import Note
class Notes:
    notes: list[Note]
    path:str
    def __init__(self,path):
        self.notes = []
        self.path = path
        self.load()

    
    def load(self):
        with (open(self.path, 'a+', encoding='utf-8')) as f:
            f.close
        with (open(self.path, 'r', encoding='utf-8')) as f:
            list_data = f.readlines()
        for record in list_data:
            list_note = record.split(';',maxsplit=3)
            note = Note(int(list_note[0]),datetime.strptime(list_note[1], '%Y-%m-%d %H:%M:%S.%f'), list_note[2], list_note[3].rstrip())
            self.notes.append(note)
    
    def get_all(self) -> str:
        result = ''
        for note in self.notes:
            result = result + str(note) + '\n'
        return result

    def get_today(self) -> str:
        result = ''
        for note in self.notes:
            if note.date_time.date() == datetime.now().date():
                result = result + str(note) + '\n'
        return result
    
    def save(self):
        lines=[]
        for note in self.notes:
            lines.append(';'.join([str(note.id),str(note.date_time),note.header,note.body]))
        with (open(self.path, 'w', encoding='utf-8')) as f:
            f.writelines(f'{line}\n' for line in lines)
    
    def add(self,note:Note):
        self.notes.append(note)
        self.save()
    
    def add(self,id,date_time,header,body):
        self.notes.append(Note(id,date_time,header,body))
        self.save()
    
    def remove(self,id:int):
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)
        self.save()
    
    def remove_all(self):
        self.notes = []
        self.save()

    def get_ids(self):
        ids=[]
        for note in self.notes:
            ids.append(note.id)
        return ids

    def sort_id(self):
        self.notes.sort(key=lambda x: x.id)    
    
    def sort_header(self):
        self.notes.sort(key=lambda x: x.header)
