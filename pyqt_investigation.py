# pyqt6_investigation.py

import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem

from member_dao import MemberDao

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Sample")
        self.setGeometry(100, 100, 600, 400)
        
        self.btn_test = QPushButton("Press Me", self)
        self.btn_test.move(10, 5)
        self.btn_test.clicked.connect(self.btn_test_clicked)

        self.dao = MemberDao()
        self.members = self.dao.get_all()

        self.member_table = QTableWidget(self)
        self.member_table.setGeometry(10, 30, 580,360)
        self.member_table.setColumnCount(4)
        self.member_table.setHorizontalHeaderLabels(["ID", "Name", "Email", "Active"])

        self.member_table.setColumnWidth(0, 90)
        self.member_table.setColumnWidth(1, 200)
        self.member_table.setColumnWidth(2, 200)
        self.member_table.setColumnWidth(3, 50)

        self.member_table.itemChanged.connect(self.member_table_item_changed)

        self.member_table.setRowCount(len(self.members))

        for row, member in enumerate(self.members):
            self.member_table.setItem(row, 0, QTableWidgetItem(str(member.id)))
            self.member_table.setItem(row, 1, QTableWidgetItem(member.name))
            self.member_table.setItem(row, 2, QTableWidgetItem(member.email))
            self.member_table.setItem(row, 3, QTableWidgetItem("Yes" if member.active else "No"))


        self.btn_delete = QPushButton("Delete", self)
        self.btn_delete.move(50, 5)
        self.btn_delete.clicked.connect(self.btn_delete_clicked)

    def member_table_item_changed(self, item):

        row = item.row()
        column = item.column()

        id = int(self.member_table.item(row, 0).text())

        member = [member for member in self.members if member.id == id][0]
        
        if column == 1:
            member.name = item.text()
        
        self.dao.update(member)





    def btn_delete_clicked(self):
        answer = QMessageBox.question(self, 
                            "Confirm Delete", 
                            "Are you sure?", 
                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                            QMessageBox.StandardButton.No)
        
        if answer == QMessageBox.StandardButton.Yes :
            selected_items = self.member_table.selectedItems()
            row = selected_items[0].row()
            id = self.member_table.item(row, 0).text()

            if self.dao.delete(int(id)) > 0:
                self.member_table.removeRow(row)





    def btn_test_clicked(self):
        QMessageBox.information(self, "Click", "You clicked the button")

    def closeEvent(self, event):
        # QMessageBox.information(self, "Closing", "The application is closing")
        self.dao.close()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())