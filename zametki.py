# Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок. Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки. Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой). Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как параметры запуска программы (команда, данные), можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента.


import json
import os
from datetime import datetime



def create_note(): #метод для создания новой заметки
    timestamp = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')# получаем текушую дату и время
    note_id = len(notes)+1#генерируем уникальный идентификатор для новой заметки
    note_title = input("Введите заголовок: ")
    note_body = input("Введите текст: ")

    note = {
        "id": note_id,
        "title": note_title,
        "body": note_body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes()
    print("заметка создана")

def read_notes(): # метод для чтения всех заметок
    for note in notes:
        print(f"ID: {note['id']}nЗаголовок:{note['title']}nТекст: {note['body']}nВремя: {note['timestamp']}n")

def edit_note(): #метод для редактирования заметки
    note_id = int(input("Введите Id заметки, которую необходимо отредактировать: "))
    note_index = -1

    for index, note in enumerate(notes):#Функция enumerate используется для упрощения прохода по коллекциям, например спискам, в цикле, когда кроме самих элементов требуется их индекс.
        if note['id']== note_id:
            note_index = index
            break
    if note_index != -1:
        note_title = input("введите нобый заголовок заметки: ") 
        note_body = input("Введите новый текст: ")
        notes[note_index]['title'] = note_title
        notes[note_index]['body'] = note_body
        notes[note_index]['timestamp'] = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
        save_notes()
        print("Заметка отредактированна")
    else:
        print("заметка не найдена")

def delete_note():# метод для удаления заметки
    note_id = int(input("Введите Id заметки, которую надо удалить: ")) 
    note_index = -1

    for index, note in enumerate(notes):
        if note['id']== note_id:
            note_index = index
            break

    if note_index != -1:
        del notes[note_index]
        save_notes()
        print("Заметка удалена")
    else:
        print("Заметка не найдена")

def save_notes(): # метод для сохранения заметок
    with open ("notes.json","w") as file:
        json.dump(notes,file)

def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json","r") as file:
            notes.extend(json.load(file))

notes = []
load_notes()
while True:
    print("nМеню:")
    print("1.Создать заметку")
    print("2.Просмотреть все заметки")
    print("3.Редактировать заметку")
    print("4.Удалить заметку")
    print("5.Выйти")

    choice = input("Выберите действие: ")
    if choice =="1":
        create_note()
    elif choice =="2":
        read_notes()
    elif choice =="3":
        edit_note()
    elif choice =="4":    
        delete_note()
    elif choice =="5":
        break 
    else:
        print("Ошибка. Введите еше раз")   




