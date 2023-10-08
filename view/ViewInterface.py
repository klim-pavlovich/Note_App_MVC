from abc import ABC, abstractclassmethod

""""
Интерфейс View
"""
class ViewInterface(ABC):
    
    # Отображение меню
    @abstractclassmethod
    def display_menu(self):
        pass
    
    # Отображение всех заметок
    @abstractclassmethod
    def display_notes(self):
        pass
    
    # Запрос комманды
    @abstractclassmethod
    def input_command(self):
        pass
    
    # Запрос информации для добавления заметки
    @abstractclassmethod
    def get_note_info(self):
        pass
    
    # Уведомление о добавлении заметки
    @abstractclassmethod
    def notify_added_note(self):
        pass
      
    # Уведомление об успешном добавлении заметки
    @abstractclassmethod
    def notify_saved_note(self):
        pass
        
    # Уведомление об успешном изменении заметки
    @abstractclassmethod
    def notify_changed_note(self, result_of_changing):
        pass
   
    @abstractclassmethod
    # Отображение одной заметки
    def display_note(self,note):
        pass
        
    # Изменение заметки по Id
    @abstractclassmethod
    def get_note_id(self):
        pass
        
    # Обработка неверно введенного Id
    @abstractclassmethod
    def error_id_process(self):
        pass
        