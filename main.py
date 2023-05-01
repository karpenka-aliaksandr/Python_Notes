from controller import Controller
from notes import Notes 
from view import View
# from note import Note
# from datetime import datetime



notes = Notes('Notes.txt')
view = View()
controller = Controller(notes, view)
controller.start()
# notes = Notes('Notes.txt')
# notes.load()
# print(notes.get_all())
# notes.add_note(Note(3,datetime.now(),'head3','body3'))
# notes.add_note(Note(5,datetime.now(),'head5','body5'))

# print('-------')
# print(notes.get_all())
# notes.delete_note(5)
# print('-------')
# print(notes.get_all())
# notes.save_notes()