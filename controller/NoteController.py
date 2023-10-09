"""
Класс NoteController - связующее звено между Model и View
"""
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
            
            if choice == '4':
                asked_id = self.view.get_note_id_for_deleting()
                answer_for_asked_id = self.model.is_existed_id(asked_id)
                if (answer_for_asked_id >= 1):
                    result_of_deleting = self.model.delete_note(asked_id)
                    self.view.delete_note(result_of_deleting)
                else:
                    self.view.error_id_process()
            
            if choice == '3':
                asked_id = self.view.get_note_id_for_changing()
                answer_for_asked_id = self.model.is_existed_id(asked_id)
                if (answer_for_asked_id >= 1):
                    old_note = self.model.get_note(asked_id)
                    self.view.display_note(old_note)
                    new_note_info = self.view.get_note_info()
                    result_of_changing = self.model.change_note(old_note,new_note_info)
                    self.view.notify_changed_note(result_of_changing)
                else:
                    self.view.error_id_process()
                
            
            if choice == '2':
                note_info = self.view.get_note_info()
                self.model.add_note(note_info)
                self.view.notify_saved_note()
                
            if choice == '1':
                all_notes = self.model.get_notes()
                self.view.display_notes(all_notes)
                
            if choice == '0':
                exitFromApp = True
                
            else:
                self.view.incorrect_menu_input_processing()