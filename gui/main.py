from PySide6.QtWidgets import QApplication
from gui.views import NotesView
from gui.controller import NotesController

def main():
    app = QApplication([])
    window = NotesView()
    controller = NotesController(window)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()