from view.ViewInterface import ViewInterface

class ConsoleView(ViewInterface):
    
    # Отображение меню
    def display_menu(self):
        print("Меню:")
        print("1. Просмотреть все заметки")
        print("2. Создать заметку")
        print("0. Выйти из приложения")
    
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
        print("Заметка успешно добавлена")
        
    # Отображение всех заметок
    def display_notes(self, notes):
        if not notes:
            print("У вас пока нет заметок.")
        else:
            print("\nВаши заметки: ")
            for note in notes:
                print(f"Id: {note.id}")
                print(f"Заголовок: {note.title}")
                print(f"Тело: {note.body}")
                print(f"Дата: {note.date}\n")