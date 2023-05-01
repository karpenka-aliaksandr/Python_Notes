sub_menu = []

def clear():
    global sub_menu
    sub_menu = []

def add(element):
    global sub_menu
    sub_menu.append(element)

def get():
    return sub_menu