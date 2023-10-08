from datetime import datetime
import json
from model.Note import Note
from model.ModelInterface import ModelInterface
from model.NoteCollection import NoteCollection

class NoteModel(ModelInterface):
    
    def __init__(self, filename):
        self.filename = filename
        self.notes = self.load_notes()
        
    def load_notes(self):
        try:
            if not (self.file_is_empty(self.filename)):
                with open (self.filename, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    if "notes" in data: 
                        note_collection = NoteCollection()
                        for note_data in data['notes']:
                            old_note = Note(note_data['id'], note_data['title'], note_data['body'], note_data['date'])
                            note_collection.add_note(old_note)
                        return note_collection
            else:
                return NoteCollection()
        except FileNotFoundError:
            self.notes = NoteCollection()
            
    def save_notes(self):
        data = {'notes': [{'id': note.id, 'title': note.title, 'body': note.body, 'date': note.date } for note in self.notes]}
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file,indent=4,ensure_ascii=False)
    
    def add_note(self, note_info):
        # self.load_notes()
        if self.notes.__len__()==0:
            max_id = 0
        else:
            max_id = max(note.id for note in self.notes)  
        new_note = Note(
            max_id + 1,
            note_info["title"],
            note_info["body"],
            datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        )
        self.notes.add_note(new_note)
        self.save_notes()
        
    def file_is_empty(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                return not bool(content)
        except FileNotFoundError:
            return True
        
    def get_notes(self):
        return self.notes