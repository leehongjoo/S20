from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout


class Ui_dialog(QtWidgets.QDialog):
    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)
        self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("Sign In")

        self.id = None
        self.password = None

        label1 = QLabel("notch Hz: ")
        label2 = QLabel("notch QualityFactor: ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.pushButton1= QPushButton("Ok")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.id = self.lineEdit1.text()
        self.password = self.lineEdit2.text()
        self.close()