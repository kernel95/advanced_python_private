# pyqt_investigation.py

import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem
from member_dao import MemberDao

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Sample")
        self.setGeometry(100,100,600,400)

        self.btn_test = QPushButton("Press Me", self)
        self.btn_test.move(10,5)
        self.btn_test.clicked.connect(self.btn_test_clicked)
        #let's import the members
        self.dao = MemberDao()
        self.members = self.dao.get_all()
        #print (self.members) #just check you got it

        #let's use the db table and put it in the gui
        self.member_table = QTableWidget(self)
        self.member_table.setGeometry(10,30,580,370) #0,0 means top left
        self.member_table.setColumnCount(4)
        self.member_table.setHorizontalHeaderLabels(["ID", "Name", "Email", "Active"])

        self.member_table.setColumnWidth(0, 50)
        self.member_table.setColumnWidth(1, 200)
        self.member_table.setColumnWidth(2, 200)
        self.member_table.setColumnWidth(3, 90)

        #add them in the gui
        self.member_table.setRowCount(len(self.members))
        for row, member in enumerate(self.members):
            self.member_table.setItem(row, 0, QTableWidgetItem(str(member.id)))
            self.member_table.setItem(row, 1, QTableWidgetItem(member.name))
            self.member_table.setItem(row, 2, QTableWidgetItem(member.email))
            self.member_table.setItem(row, 3, QTableWidgetItem("Yes" if member.active else "No"))



    def btn_test_clicked(self):
        QMessageBox.information(self, "Click", "You clicked the button") #debugging 


    def closeEvent(self, event):
        #QMessageBox.information(self, "Closing db", "The application is closing")
        self.dao.close()
        #return super().closeEvent(event)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())