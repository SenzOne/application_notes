import json
import os
from datetime import datetime


# Функция для загрузки заметок из файла JSON, если файл существует
def load_notes():
    if os.path.exists('notes.json'):
        with open('notes.json', 'r', encoding="UTF-8") as file:
            return json.load(file)
    else:
        return {}


# Функция для сохранения заметок в файл JSON
def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)


# Функция для добавления новой заметки
def add_note(notes):
    note_id = input("Введите идентификатор заметки: ")
    if note_id in notes:
        print("Заметка с таким идентификатором уже существует.")
        return

    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes[note_id] = {
        "title": title,
        "body": body,
        "created_at": current_time,
        "last_updated_at": current_time
    }
    save_notes(notes)
    print("Заметка успешно добавлена.")


# Функция для отображения всех заметок
def display_notes(notes):
    if not notes:
        print("Нет доступных заметок.")
        return

    print("Список заметок:")
    for note_id, note_info in notes.items():
        print(f"Идентификатор: {note_id}")
        print(f"Заголовок: {note_info['title']}")
        print(f"Дата создания: {note_info['created_at']}")
        print(f"Дата последнего изменения: {note_info['last_updated_at']}")
        print("=" * 20)


# Функция для редактирования заметки
def edit_note(notes):
    note_id = input("Введите идентификатор заметки для редактирования: ")
    if note_id not in notes:
        print("Заметка с таким идентификатором не существует.")
        return

    print("Текущая информация о заметке:")
    print(f"Идентификатор: {note_id}")
    print(f"Заголовок: {notes[note_id]['title']}")
    print(f"Текст заметки: {notes[note_id]['body']}")
    print("=" * 20)

    new_title = input("Введите новый заголовок (оставьте пустым, чтобы оставить прежний): ")
    new_body = input("Введите новый текст заметки (оставьте пустым, чтобы оставить прежний): ")

    if new_title:
        notes[note_id]['title'] = new_title
    if new_body:
        notes[note_id]['body'] = new_body

    notes[note_id]['last_updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_notes(notes)
    print("Заметка успешно отредактирована.")


# Функция для удаления заметки
def delete_note(notes):
    note_id = input("Введите идентификатор заметки для удаления: ")
    if note_id not in notes:
        print("Заметка с таким идентификатором не существует.")
        return

    del notes[note_id]
    save_notes(notes)
    print("Заметка успешно удалена.")


def main():
    notes = load_notes()

    while True:
        print("\n===== Меню =====")
        print("1. Просмотреть заметки")
        print("2. Добавить новую заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            display_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            edit_note(notes)
        elif choice == '4':
            delete_note(notes)
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите существующий вариант.")


if __name__ == "__main__":
    main()
