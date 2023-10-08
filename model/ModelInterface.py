from abc import ABC, abstractclassmethod

"""
Интерфейс модели
"""

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
    
    # Получение всех заметок
    @abstractclassmethod
    def get_notes(self):
        pass
    
    # Изменение заметки по id
    @abstractclassmethod
    def change_note(self, new_note_info):
        pass