# pyqt_async_investigation.py

import json
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QListWidget, QListWidgetItem
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt6.QtCore import Qt,QUrl
import requests


URL = "https://api.acodingtutor.com/members?_delay=5000"

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.count = 0

        self.lbl_info = QLabel(self)
        self.lbl_info.setGeometry(100, 0, 100, 200)
        self.lbl_info.setText(f"Count: {self.count}")

        self.btn_plus = QPushButton("+", self)
        self.btn_plus.setGeometry(100, 40, 50, 50)
        self.btn_plus.clicked.connect(self.btn_plus_clicked)

        self.btn_minus = QPushButton("-", self)
        self.btn_minus.setGeometry(150, 40, 50, 50)
        self.btn_minus.clicked.connect(self.btn_minus_clicked)

        self.btn_fetch = QPushButton("Fetch", self)
        self.btn_fetch.setGeometry(100, 120, 100, 30)
        self.btn_fetch.clicked.connect(self.btn_fetch_clicked)

        self.btn_fetch_async = QPushButton("Fetch(async)", self)
        self.btn_fetch_async.setGeometry(100, 160, 100, 30)
        self.btn_fetch_async.clicked.connect(self.btn_fetch_async_clicked)

        # for async calls use this
        self.net = QNetworkAccessManager(self)

        self.member_list = QListWidget(self)
        self.member_list.setGeometry(300, 20, 100, 200)
        self.member_list.itemClicked.connect(self.on_member_list_clicked)

    def on_member_list_clicked(self, item:QListWidgetItem):
        print (item.text())
        member = item.data(Qt.ItemDataRole.UserRole)
        QMessageBox.information(self, "You chose", str(member))

    def btn_fetch_clicked(self):
        response = requests.get(URL)
        data = response.json()
        QMessageBox.information(self, "Click", str(data))
        
    def btn_fetch_async_clicked(self):
        print ("fetch async")
        reply = self.net.get(QNetworkRequest(QUrl(URL)))
        reply.finished.connect(lambda: self.on_done(reply))

    def on_done(self, reply):

        if reply.error() == QNetworkReply.NetworkError.NoError:
            text = reply.readAll().data().decode("utf-8", "replace")
            members = json.loads(text)
            for member in members:
                item = QListWidgetItem(member['name'])
                item.setData(Qt.ItemDataRole.UserRole, member)
                self.member_list.addItem(item)


                #self.member_list.addItem(QListWidgetItem(member['name']))
        

    def btn_plus_clicked(self):
        self.count += 1
        self.lbl_info.setText(f"Count: {self.count}")

    def btn_minus_clicked(self):
        self.count -= 1
        self.lbl_info.setText(f"Count: {self.count}")
    

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = App()
    window.show()

    sys.exit(app.exec())