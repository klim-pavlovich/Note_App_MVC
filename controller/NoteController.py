class NoteController:
    
    def __init__(self,model,view):
        self.model = model
        self.view = view()
        
    def run(self):
        exitFromApp = False
        while(exitFromApp == False):
            self.view.display_menu()
            choice = self.view.input_command()
            
            if choice == '2':
                note_info = self.view.get_note_info()
                self.model.add_note(note_info)
                self.view.notify_saved_note()
                
            if choice == '0':
                exitFromApp = True