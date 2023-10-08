"""
Основная сущность - класс Заметка

@param id - идентификатор
@param title - заголовок
@param body - тело заметки
@param date - дата создания заметки
"""
class Note:
    # Инициализация заметки
    def __init__(self, id, title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date