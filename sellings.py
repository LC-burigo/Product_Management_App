import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3

con = sqlite3.connect("products.db")
cur = con.cursor()

class SellProducts(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sell Products")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(40, 150, 350, 600)
        self.setFixedSize(self.size())
        self.UI()
        self.show()
    
    def UI(self):
        self.widgets()
        self.layouts()
    
    def widgets(self):
        ###########################widgets of top layout#######################
        self.sellProductImg = QLabel()
        self.img = QPixmap('icons/shop.png')
        self.sellProductImg.setPixmap(self.img)
        self.sellProductImg.setAlignment(Qt.AlignCenter)
        self.titleText = QLabel("Sell Product")
        self.titleText.setAlignment(Qt.AlignCenter)
        ###########################widgets of bottom layout####################
        self.productCombo = QComboBox()
        self.memberCombo = QComboBox()
        self.quantityCombo = QComboBox()
        self.submitBtn = QPushButton("Submit")
        #self.submitBtn.clicked.connect(self.)

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.bottomFrame = QFrame()
        ##############################add widgets#####################
        ###########################widgets of top layouts##########################
        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.sellProductImg)
        self.topFrame.setLayout(self.topLayout)
        ###########################widgets of form layouts##########################
        self.bottomLayout.addRow(QLabel("Product: "), self.productCombo)
        self.bottomLayout.addRow(QLabel("member: "), self.memberCombo)
        self.bottomLayout.addRow(QLabel("quantity: "), self.quantityCombo)
        self.bottomLayout.addRow(QLabel(""), self.submitBtn)
        self.bottomFrame.setLayout(self.bottomLayout)

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.setLayout(self.mainLayout)