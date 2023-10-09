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
            
            # Удаление заметки
            if choice == '4':
                asked_id = self.view.get_note_id_for_deleting()
                try:
                    is_int_asked_id = int(asked_id)
                    if is_int_asked_id:
                        answer_for_asked_id = self.model.is_existed_id(is_int_asked_id)
                        if (answer_for_asked_id >= 1):
                            result_of_deleting = self.model.delete_note(asked_id)
                            self.view.delete_note(result_of_deleting)
                        else:
                            self.view.error_id_process()
                except ValueError:
                    self.view.incorrect_input_type_id_process() 

            # Изменение заметки
            elif choice == '3':
                type_of_changing = self.view.get_type_info_to_change()
                
                # Изменение только заголовка заметки
                if type_of_changing == '1':
                    asked_id = self.view.get_note_id_for_changing()
                    try:
                        is_int_asked_id = int(asked_id)
                        if is_int_asked_id:
                            answer_for_asked_id = self.model.is_existed_id(is_int_asked_id)
                            if (answer_for_asked_id >= 1):
                                old_note = self.model.get_note(is_int_asked_id)
                                self.view.display_note(old_note)
                                new_head_note_info = self.view.get_new_head_note_info()
                                result_of_changing = self.model.change_head_note(old_note,new_head_note_info)
                                self.view.notify_changed_head_note(result_of_changing)
                            else:
                                self.view.error_id_process() # если в базе нет заметки с введенным id
                    except ValueError:
                        self.view.incorrect_input_type_id_process() # если пользователь ввел не int
                
                # Изменение только тела заметки  
                elif type_of_changing == '2':
                    asked_id = self.view.get_note_id_for_changing()
                    try:
                        is_int_asked_id = int(asked_id)
                        if is_int_asked_id:
                            answer_for_asked_id = self.model.is_existed_id(is_int_asked_id)
                            if (answer_for_asked_id >= 1):
                                old_note = self.model.get_note(is_int_asked_id)
                                self.view.display_note(old_note)
                                new_body_note_info = self.view.get_new_body_note_info()
                                result_of_changing = self.model.change_body_note(old_note,new_body_note_info)
                                self.view.notify_changed_body_note(result_of_changing)
                            else:
                                self.view.error_id_process() # если в базе нет заметки с введенным id
                    except ValueError:
                        self.view.incorrect_input_type_id_process() # если пользователь ввел не int
                
                # Изменение и заголовка и тела заметки
                elif type_of_changing == '3':
                    asked_id = self.view.get_note_id_for_changing()
                    try:
                        is_int_asked_id = int(asked_id)
                        if is_int_asked_id:
                            answer_for_asked_id = self.model.is_existed_id(is_int_asked_id)
                            if (answer_for_asked_id >= 1):
                                old_note = self.model.get_note(is_int_asked_id)
                                self.view.display_note(old_note)
                                new_note_info = self.view.get_note_info()
                                result_of_changing = self.model.change_note(old_note,new_note_info)
                                self.view.notify_changed_note(result_of_changing)
                            else:
                                self.view.error_id_process() # если в базе нет заметки с введенным id
                    except ValueError:
                        self.view.incorrect_input_type_id_process() # если пользователь ввел не int
                else:
                    self.view.incorrect_menu_input_processing()
            
            # Создание заметки        
            elif choice == '2':
                note_info = self.view.get_note_info()
                self.model.add_note(note_info)
                self.view.notify_saved_note()
            
            # Просмотр заметок  
            elif choice == '1':
                all_notes = self.model.get_notes()
                self.view.display_notes(all_notes)
            
            # Выход из приложения    
            elif choice == '0':
                exitFromApp = True
            
            # Обработка неверного ввода    
            else:
                self.view.incorrect_menu_input_processing()