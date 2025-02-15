from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTableWidget, QHeaderView

class NotesView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Take Note")

        # layouts
        self.central_widget = QWidget()
        self.main_layout = QVBoxLayout()

        # widgets
        self.add_note_input = QLineEdit()
        self.add_note_input.setPlaceholderText("Enter note")

        self.add_note_button = QPushButton("Add Note")
        self.list_notes_button = QPushButton("List Notes")
        self.delete_note_button = QPushButton("Delete Note(s)")

        self.notes_display = QTableWidget()
        self.notes_display.setColumnCount(1)
        self.notes_display.setHorizontalHeaderLabels(["Messages"])
        header = self.notes_display.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)  # First column stretches

        # row 1 layout
        self.layout_1 = QHBoxLayout()
        self.layout_1.addWidget(self.add_note_button)
        self.layout_1.addWidget(self.delete_note_button)

        # row 2 layout
        self.layout_2 = QHBoxLayout()
        self.layout_2.addWidget(self.list_notes_button)

        # all buttons
        self.layout_3 = QVBoxLayout()
        self.layout_3.addLayout(self.layout_1)
        self.layout_3.addLayout(self.layout_2)

        # add widgets to layout
        self.main_layout.addWidget(self.add_note_input)
        self.main_layout.addLayout(self.layout_3)
        self.main_layout.addWidget(self.notes_display)

        # set layout
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)