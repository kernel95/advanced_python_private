# pyqt_async_investigation.py

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

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
        pass

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