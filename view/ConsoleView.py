from view.ViewInterface import ViewInterface

class ConsoleView(ViewInterface):
    
    # Отображение меню
    def display_menu(self):
        print("Меню:")
        print("1. Просмотреть все заметки")
        print("2. Создать заметку")
        print("3. Изменить заметку по id")
        print("4. Удалить заметку по id")
        print("0. Выйти из приложения\n")
    
    # Получение выбора команды от пользователя
    def input_command(self):
        return input("\nВыберите команду: ")
    
    # Получение информации о заметке от пользователя
    def get_note_info(self):
        title = input("\nВведите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        return {"title":title,"body":body}
    
    # Получение нового заголовка заметки для изменения заметки
    def get_new_head_note_info(self):
        title = input("\nВведите новый заголовок заметки: ")
        return {"title":title}
    
    # Получение нового тела заметки для изменения заметки
    def get_new_body_note_info(self):
        body = input("\nВведите новый текст заметки: ")
        return {"body":body}
    
    # Уведомление об изменении заголовка заметки
    def notify_changed_head_note(self, result_of_changing):
        if result_of_changing == 1:
            print("\nЗаголовок заметки был успешно изменен.\n")
        else:
            print("\nНе удалось изменить заголовок заметки.\n")
    
    # Уведомление об изменении тела заметки
    def notify_changed_body_note(self, result_of_changing):
        if result_of_changing == 1:
            print("\nТекст заметки был успешно изменен.\n")
        else:
            print("\nНе удалось изменить текст заметк.\n")
    
    # Уведомление об успешном добавлении заметки
    def notify_saved_note(self):
        print("\nЗаметка успешно добавлена.\n")
        
    # Уведомление об изменении заметки
    def notify_changed_note(self, result_of_changing):
        if result_of_changing == 1:
            print("\nЗаметка успешно изменена.\n")
        else:
            print("\nНе удалось изменить заметку.\n")
        
    # Отображение всех заметок
    def display_notes(self, notes):
        if not notes:
            print("\nУ вас пока нет заметок.\n")
        else:
            print("\nВаши заметки: ")
            for note in notes:
                print(f"Id: {note.id}")
                print(f"Заголовок: {note.title}")
                print(f"Тело: {note.body}")
                print(f"Дата: {note.date}\n")
                
    # Отображение одной заметки
    def display_note(self,note):
        print(f"Заголовок: {note.title}")
        print(f"Тело: {note.body}")
        print(f"Дата: {note.date}\n")
        
    # Получение информации о том, что хочет изменить пользователь в заметке
    def get_type_info_to_change(self):
        print("\nЧтобы изменить заметку выберите один из следующих пунктов:")
        print("1. Изменить заголовок;")
        print("2. Изменить текст;")
        print("3. Изменить и заголовок и текст заметки.")
        type_info = input("\nВаш выбор: ")
        return type_info
        
    # Получение id заметки для изменения
    def get_note_id_for_changing(self):
        id = input("\nВведите Id заметки, которую хотите изменить: ")
        return id
        
    # Получение id заметки для удаления
    def get_note_id_for_deleting(self):
        id = input("\nВведите Id заметки, которую хотите удалить: ")
        return id
    
    # Обработка неверно введенного Id (в базе нет такого id)
    def error_id_process(self):
        print("\nЗаметки с таким Id не существует.\n")
        
    # Обработка неверно введеного типа данных для ввода id
    def incorrect_input_type_id_process(self):
        print("\nВведен неверный тип данных, 'id' заметки представляет собой целое число.\n")
        
    # Уведомление об удалении
    def delete_note(self, result):
        if result == 1:
            print("\nЗаметка успешно удалена.\n")
        else:
            print("\nПроизошла ошибка при удалении.\n")
        
    # Обработка неверно введеного пункта меню
    def incorrect_menu_input_processing(self):
        print("\nЯ не умею обрабатывать такие комманды. Введите пункт меню.\n")