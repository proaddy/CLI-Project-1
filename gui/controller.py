from logic.note_operations import add_note, read_notes, delete_notes
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

class NotesController:
    def __init__(self, view):
        self.view = view
        self.setup_connections()

    def setup_connections(self):
        self.view.add_note_button.clicked.connect(self.add_note)
        self.view.list_notes_button.clicked.connect(self.list_notes)
        self.view.delete_note_button.clicked.connect(self.delete_notes)
    
    def add_note(self):
        note = self.view.add_note_input.text()
        notes_len = len(read_notes())
        if note:
            item_msg = QTableWidgetItem(note)
            self.view.notes_display.insertRow(notes_len)
            self.view.notes_display.setItem(notes_len, 0, item_msg)
            add_note(note)
            QMessageBox.information(self.view, "Success", "Note added successfully!")
        else:
            QMessageBox.warning(self.view, "Warning", "Note cannot be empty.")

    def list_notes(self):
        notes = read_notes()
        self.view.notes_display.setRowCount(len(notes))
        if notes:
            for index, note in enumerate(notes):
                item_msg = QTableWidgetItem(note[1])
                self.view.notes_display.setItem(index, 0, item_msg)
        else:
            QMessageBox.warning(self.view, "Warning", "No notes found.")
    
    def delete_notes(self):
        selected = set(index.row() for index in self.view.notes_display.selectedIndexes())
        if selected:
            for row in sorted(selected, reverse=True): # to avoid row shifting we shift the row
                self.view.notes_display.removeRow(row)
            delete_notes(selected)
            QMessageBox.information(self.view, "Success", "Note(s) deleted successfully!")
        else:
            QMessageBox.warning(self.view, "Warning", "No note(s) selected!")
        
