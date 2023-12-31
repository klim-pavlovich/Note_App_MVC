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
    def change_note(self, old_note, new_note_info):
        pass
    
    # Изменение заголовка заметки по id
    @abstractclassmethod
    def change_head_note(self, old_note, new_head_note_info):
        pass
    
    # Изменение тела заметки по id
    @abstractclassmethod
    def change_body_note(self, old_note, new_body_note_info):
        pass
    
    # Проверка на то, пустой ли файл
    @abstractclassmethod
    def file_is_empty(self, filename):
        pass
    
    # Проверка на существование заметки по id
    @abstractclassmethod
    def is_existed_id(self,id):
        pass
    
    # Получение заметки по id   
    @abstractclassmethod    
    def get_note(self,id):
        pass
    
    # Удаление заметки по id
    @abstractclassmethod
    def delete_note(self,id):
        pass
    
    