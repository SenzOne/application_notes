from datetime import datetime
import json
import os


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
