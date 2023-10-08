from abc import ABC, abstractclassmethod

class ModelInterface(ABC):
    
    # Инициализация модели
    @abstractclassmethod
    def __init__(self,filename):
        pass
    
    # Загрузка заметок
    @abstractclassmethod
    def load_notes(self):
        pass
    
    # Сохранение заметок
    @abstractclassmethod
    def save_notes(self):
        pass
    
    # Добавление заметки
    @abstractclassmethod
    def add_note(self):
        pass