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
        pass