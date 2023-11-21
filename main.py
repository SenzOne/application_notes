import json
import os
from datetime import datetime


class NoteModel:
    def __init__(self, file_name='notes.json'):
        self.file_name = file_name
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            return {}

    def save_notes(self):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(self.notes, file, ensure_ascii=False, indent=4)

    def add_note(self, note_id, title, body):
        if note_id in self.notes:
            return False, "Заметка с таким идентификатором уже существует."

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.notes[note_id] = {
            "title": title,
            "body": body,
            "created_at": current_time,
            "last_updated_at": current_time
        }
        self.save_notes()
        return True, "Заметка успешно добавлена."

    def edit_note(self, note_id, new_title, new_body):
        if note_id not in self.notes:
            return False, "Заметка с таким идентификатором не существует."

        if new_title:
            self.notes[note_id]['title'] = new_title
        if new_body:
            self.notes[note_id]['body'] = new_body

        self.notes[note_id]['last_updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_notes()
        return True, "Заметка успешно отредактирована."

    def delete_note(self, note_id):
        if note_id not in self.notes:
            return False, "Заметка с таким идентификатором не существует."

        del self.notes[note_id]
        self.save_notes()
        return True, "Заметка успешно удалена."


class NoteView:
    @staticmethod
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


class NoteController:
    def __init__(self):
        self.model = NoteModel()
        self.view = NoteView()

    def display_notes(self):
        self.view.display_notes(self.model.notes)

    def add_note(self):
        note_id = input("Введите идентификатор заметки: ")
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        success, message = self.model.add_note(note_id, title, body)
        if success:
            print(message)
        else:
            print(f"Ошибка: {message}")

    def edit_note(self):
        note_id = input("Введите идентификатор заметки для редактирования: ")
        new_title = input("Введите новый заголовок (оставьте пустым, чтобы оставить прежний): ")
        new_body = input("Введите новый текст заметки (оставьте пустым, чтобы оставить прежний): ")
        success, message = self.model.edit_note(note_id, new_title, new_body)
        if success:
            print(message)
        else:
            print(f"Ошибка: {message}")

    def delete_note(self):
        note_id = input("Введите идентификатор заметки для удаления: ")
        success, message = self.model.delete_note(note_id)
        if success:
            print(message)
        else:
            print(f"Ошибка: {message}")


def main():
    controller = NoteController()

    while True:
        print("\n===== Меню =====")
        print("1. Просмотреть заметки")
        print("2. Добавить новую заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            controller.display_notes()
        elif choice == '2':
            controller.add_note()
        elif choice == '3':
            controller.edit_note()
        elif choice == '4':
            controller.delete_note()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите существующий вариант.")


if __name__ == "__main__":
    main()
