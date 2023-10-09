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
        return input("Выберите команду: ")
    
    # Получение информации о заметке от пользователя
    def get_note_info(self):
        title = input("\nВведите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        return {"title":title,"body":body}
    
    # Уведомление об успешном добавлении заметки
    def notify_saved_note(self):
        print("Заметка успешно добавлена.\n")
        
    # Уведомление об успешном изменении заметки
    def notify_changed_note(self, result_of_changing):
        if result_of_changing == 1:
            print("Заметка успешно изменена.\n")
        else:
            print("Не удалось изменить заметку.\n")
        
    # Отображение всех заметок
    def display_notes(self, notes):
        if not notes:
            print("У вас пока нет заметок.\n")
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
        
    # Получение id заметки для изменения
    def get_note_id_for_changing(self):
        id = input("\nВведите Id заметки, которую хотите изменить: ")
        return id
        
    # Получение id заметки для удаления
    def get_note_id_for_deleting(self):
        id = input("\nВведите Id заметки, которую хотите удалить: ")
        return id
    
    # Обработка неверно введенного Id
    def error_id_process(self):
        print("\nЗаметки с таким Id не существует.\n")
        
    # Уведомление об удалении
    def delete_note(self, result):
        if result == 1:
            print("\nЗаметка успешно удалена.\n")
        else:
            print("\nПроизошла ошибка при удалении.\n")
        
    # Обработка неверно введеного пункта меню
    def incorrect_menu_input_processing(self):
        print("\nЯ не умею обрабатывать такие комманды. Введите пункт меню.\n")
        
    # Обработка неверно введеного типа данных для ввода id
    def incorrect_input_type_id_process(self):
        print("\nВведен неверный тип данных, 'id' заметки представляет собой целое число.\n")