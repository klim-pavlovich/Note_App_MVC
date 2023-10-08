from datetime import datetime
import json
from model.Note import Note
from model.ModelInterface import ModelInterface
from model.NoteCollection import NoteCollection

class NoteModel(ModelInterface):
    
    def __init__(self, filename):
        self.filename = filename
        self.notes = NoteCollection()
        
    def load_notes(self):
        try:
            with open (self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.notes = [Note(note['id'], note['title'], note['body'], note['date'] ) for note in data]
        except FileNotFoundError:
            self.notes=[]
            
    def save_notes(self):
        data = {'notes': [{'id': note.id, 'tittle': note.title, 'body': note.body, 'date': note.date } for note in self.notes.notes]}
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file,indent=4,ensure_ascii=False)
            
    def add_note(self, note_info):
        new_id = len(self.notes) + 1
        new_note = Note(
            new_id,
            note_info["title"],
            note_info["body"],
            datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        )
        self.notes.add_note(new_note)
        self.save_notes()