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
      
    # Уведомление об успешном добавлении заметки
    @abstractclassmethod
    def notify_saved_note(self):
        pass
        
    # Получение информации о том, что хочет изменить пользователь в заметке
    @abstractclassmethod
    def get_type_info_to_change(self):
        pass
        
    # Получение нового заголовка заметки для изменения заметки
    @abstractclassmethod
    def get_new_head_note_info(self):
        pass
    
    # Получение нового тела заметки для изменения заметки
    @abstractclassmethod
    def get_new_body_note_info(self):
        pass
    
    # Уведомление об изменении заметки
    @abstractclassmethod
    def notify_changed_note(self, result_of_changing):
        pass
    
    # Уведомление об изменении заголовка заметки
    @abstractclassmethod
    def notify_changed_head_note(self, result_of_changing):
        pass
    
    # Уведомление об изменении тела заметки
    @abstractclassmethod
    def notify_changed_body_note(self, result_of_changing):
        pass
    
    
    # Отображение одной заметки
    @abstractclassmethod
    def display_note(self,note):
        pass
        
    # Изменение заметки по Id
    @abstractclassmethod
    def get_note_id_for_changing(self):
        pass
        
    # Обработка неверно введенного Id
    @abstractclassmethod
    def error_id_process(self):
        pass
    
    # Обработка неверно введеного типа данных для ввода id
    @abstractclassmethod
    def incorrect_input_type_id_process(self):
        pass
        
    # Обработка неверно введеного пункта меню
    @abstractclassmethod
    def incorrect_menu_input_processing(self):
        pass