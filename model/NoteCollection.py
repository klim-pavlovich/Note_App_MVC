from model.Note import Note

class NoteCollection:
    
    def __init__(self):
        self.notes = []
        
    def add_note(self, note: Note):
        if isinstance(note,Note):
            self.notes.append(note)
        else:
            raise ValueError("Попытка добавить объект другого типа в коллекцию.")
        
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.notes):
            result = self.notes[self.index]
            self.index += 1
            return result
        raise StopIteration
        
    def __len__(self):
        return len(self.notes)