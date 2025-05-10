from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QLabel ,QListWidget, QLineEdit, QTextEdit , QHBoxLayout,QVBoxLayout, QFormLayout,QInputDialog

import json

app = QApplication([])

notes = {
    'Добро пожаловать' :{
        'текст' :'это лучшее приложение для заметок в мире!',
    'теги' : ['добро','пожаловать']
    }
}

with open('notes_data.json','w') as file:
    json.dump(notes,file)


notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки')
notes_win.resize(900,600)

list_notes =  QListWidget()
list_notes_label = QLabel("Список заметок")

button_note_create = QPushButton('Создать заметку')
button_note_del = QPushButton('Удать заметку')
button_not_save = QPushButton('Созранить заметку')

field_tag = QLineEdit(' ')
field_tag.setPlaceholderText('Введите тег...')
field_text = QTextEdit()
button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегов')

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_not_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1,stretch = 2)
layout_notes.addLayout(col_2,stretch = 1)
notes_win.setLayout(layout_notes)

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    for note in notes:
        if note[0] == key:
            field_text.setText(note[1])
            list_tags.clear()
            list_tags.addItems(note[2])

def add_note():
    note_name,ok = QInputDialog.getText(notes_win,'Добавть заметку','Название заметки:')
    if ok and note_name != '':
        note = list()
        note = [note_name,'',[]]
        notes.appens(note)
        list_notes.addItem(note[0])
        list_tags.addItems(note[2])
        print(notes)
        with open(str(len(notes)-1)+'.txt','w')as file:
            file.write(note[0]+'\n')


def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        index = 0
        for notte in notes:
            if note[0] == key:
                note[1] = field_text.toPlainText()
                with open(str(index)+'.txt', 'w') as file:
                      file.write(note[0]+'\n')
                      file.write(note[1]+'\n')
                      for tag in note[2]:
                        file.write(tag+' ')
                        file.write('\n')
                index += 1
            print(notes)
        else:
            print('Заметка для сохранения не выбрана!')


# def add_tag():
#     if list_notes.selectedItems():
#         key = list_notes.selectedItems()[0].text()
#         tag = field_text()
#         if not tag in notes[key]['теги']:
#             notes[key]['теги'].append(tag)
#             list_tags.addItem(tag)
#             field_tag.clear()
#             with open('notes_data.json','w') as file:
#                 json.dump(notes,file,sort_keys=True,ensure_ascii=False)
#         print(notes)
#     else:
#         print('Заметка для добавления тега не выбрана!')

button_note_create.clicked.connect(add_note)
list_notes.itemClicked.connect(show_note)
button_not_save.clicked.connect(save_note)


# with open('notes_data.json','r') as file:
#     notes = json.load(file)
#     list_notes.addItems(notes)

    # def del_note():
    #     if list_notes.selectedItems():
    #         key = list_notes.selectedItems()[0].text()
    #         del notes[key]
    #         list_notes.clear
    #         list_tags.clear
    #         field_text.clear
    #         list_notes.addItems(notes)
    #         if list_notes.selectedItems():
    #             with open('notes_data.json','w') as file:
    #                 json.dump(notes,file,sort_keys=True,ensure_ascii=False)
    #         print(notes)
    #     else:
    #         print('Заметка для удаления не выбрана')

# def del_tag():
#     if list_tags.selectedItems():
#         key = list_notes.selectedItems()[0].text()
#         tag = list_notes.selectedItems()[0].text()
#         notes[key]['теги'].remove(tag)
#         list_tags.clear()
#         list_tags.addItems(notes[key]['теги'])
#         with open('notes_data.json','w') as file:
#             json.dump(notes,file,sort_keys=True,ensure_ascii=False)
#         print(notes)
#     else:
#         print('Тег для удаления не выбран!')

# def search_tag():
#     print(button_tag_search())
#     tag = field_tag.text()
#     if button_tag_search.text() == 'Искать заметки по тегу' and tag:
#         print(tag)
#         notes_filtered = {}
#         for note in notes:
#             if tag in notes[note]['теги']:
#                 notes_filtered[note]=notes[note]
#         button_tag_search.setText('Сбросить поиск')
#         list_notes.clear()
#         list_tags.clear()
#         list_notes.addItems(notes_filtered)
#         print(button_tag_search())
#     elif button_tag_search.text() == 'Сбросить поиск':
#         field_tag.clear()
#         list_notes.clear()
#         list_tags.clear()
#         list_notes.addItems(notes)
#         button_tag_search.setText('Искать заметки по тегу')
#         print(button_tag_search.text())
#     else:
#         pass


# button_note_del.clicked.connect(del_note)
# button_tag_add.clicked.connect(add_tag)
# button_tag_del.clicked.connect(del_tag)
# button_tag_search.clicked.connect(search_tag)



notes_win.show()

name = 0
note = []
while True:
    filename = str(name)+'.txt'
    try:
        with open(filename,'r') as file:
            for line in file:
                line = line.replace('\n','')
                note.append(line)
        tags = note[2].split(' ')
        note[2] = tags

        notes.append(note)
        note = []
        name += 1

    except IOError:
        break
    
print(notes)
for note in notes:
    list_notes.addItem(note[0])


app.exec_()


