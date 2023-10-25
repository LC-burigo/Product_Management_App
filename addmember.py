import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3


con = sqlite3.connect("products.db")
cur = con.cursor()


class AddMember(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Member")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(40, 150, 350, 550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        ###########################widgets of top layout#######################
        self.addMemberImg = QLabel()
        self.img = QPixmap('icons/addmember.png')
        self.addMemberImg.setPixmap(self.img)
        self.addMemberImg.setAlignment(Qt.AlignCenter)
        self.titleText = QLabel("Add Member")
        self.titleText.setAlignment(Qt.AlignCenter)
        ###########################widgets of bottom layout####################
        self.nameEntry = QLineEdit()
        self.nameEntry.setPlaceholderText("Enter name of member")
        self.surnameEntry = QLineEdit()
        self.surnameEntry.setPlaceholderText("Enter surname of member")
        self.phoneEntry = QLineEdit()
        self.phoneEntry.setPlaceholderText("Enter phone number")
        self.submitBtn = QPushButton("Submit")

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.bottomFrame = QFrame()
        ###########################add widgets##########################
        ###########################widgets of top layouts##########################
        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.addMemberImg)
        self.topFrame.setLayout(self.topLayout)
        ###########################widgets of form layouts##########################
        self.bottomLayout.addRow(QLabel("Name: "), self.nameEntry)
        self.bottomLayout.addRow(QLabel("Surname: "), self.surnameEntry)
        self.bottomLayout.addRow(QLabel("Phone: "), self.phoneEntry)
        self.bottomLayout.addRow(QLabel(""), self.submitBtn)
        self.bottomFrame.setLayout(self.bottomLayout)

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.setLayout(self.mainLayout)
