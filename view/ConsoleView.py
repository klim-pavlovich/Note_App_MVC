from view.ViewInterface import ViewInterface

class ConsoleView(ViewInterface):
    
    def display_menu(self):
        print("Меню:")
        print("1. Просмотреть заметки")
        print("2. Создать заметку")
        print("0. Выйти из приложения")
        
    def input_command(self):
        return input("Выберите команду:")
    
    def get_note_info(self):
        title = input("Введите заголовок заметки:")
        body = input("Введите текст заметки:")
        return {"title":title,"body":body}
    
    def notify_saved_note(self):
        print("Заметка успешно добавлена")
        
    # еще нереализовано
    def display_notes(self):
        pass