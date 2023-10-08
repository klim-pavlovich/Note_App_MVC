from controller.NoteController import NoteController
from model.NoteModel import NoteModel
from view.ConsoleView import ConsoleView

def main():
    controller = NoteController(NoteModel("all_notes.json"), ConsoleView)
    controller.run()

if __name__ == "__main__":
    main()