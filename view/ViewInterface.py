from abc import ABC, abstractclassmethod

class ViewInterface(ABC):
    
    # Отображение меню
    def display_menu(self):
        pass
    
    # Отображение всех заметок
    def display_notes(self):
        pass
    
    # Запрос комманды
    def input_command(self):
        pass
    
    # Запрос информации для добавления заметки
    def get_note_info(self):
        pass
    
    # Уведомление о добавлении заметки
    def notify_added_note(self):
        pass