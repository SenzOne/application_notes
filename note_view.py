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
