# Класс NoteController - связующее звено между Model и View
class NoteController:
    
    # Инициализация контроллера
    def __init__(self,model,view):
        self.model = model
        self.view = view()
    
    # Работа контроллера    
    def run(self):
        exitFromApp = False
        while(exitFromApp == False):
            self.view.display_menu()
            choice = self.view.input_command()
            
            if choice == '2':
                note_info = self.view.get_note_info()
                self.model.add_note(note_info)
                self.view.notify_saved_note()
                
            if choice == '1':
                all_notes = self.model.get_notes()
                self.view.display_notes(all_notes)
                
            if choice == '0':
                exitFromApp = True