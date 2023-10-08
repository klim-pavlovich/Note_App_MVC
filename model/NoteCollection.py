from model.Note import Note
"""
Коллекция заметок

Предназначена для манипулирования всеми заметками
"""

class NoteCollection:
    # Инициализация коллекции заметок
    def __init__(self):
        self.notes = []
    
    # Добавление заметки    
    def add_note(self, note: Note):
        if isinstance(note,Note):
            self.notes.append(note)
        else:
            raise ValueError("Попытка добавить объект другого типа в коллекцию.")
        
    # Инициализация итератора для коллекции
    def __iter__(self):
        self.index = 0
        return self
    
    # Получение следующего элемента при итерации по коллекции
    def __next__(self):
        if self.index < len(self.notes):
            result = self.notes[self.index]
            self.index += 1
            return result
        raise StopIteration
    
    # Получение длины коллекции    
    def __len__(self):
        return len(self.notes)