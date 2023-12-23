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
        self.productCombo.currentIndexChanged.connect(self.changeComboValue)
        self.memberCombo = QComboBox()
        self.quantityCombo = QComboBox()
        self.submitBtn = QPushButton("Submit")
        self.submitBtn.clicked.connect(self.sellProduct)
        
        query = "SELECT * FROM products WHERE product_availability=?"
        products= cur.execute(query, ('Available',)).fetchall()
        query2 = "SELECT member_id, member_name FROM members"
        members= cur.execute(query2).fetchall()
        quantity = products[0][4]

        for product in products:
            self.productCombo.addItem(product[1], product[0])

        for member in members:
            self.memberCombo.addItem(member[1], member[0])

        for i in range(1, quantity+1):
            self.quantityCombo.addItem(str(i))

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

    def changeComboValue(self):
        self.quantityCombo.clear()
        product_id = self.productCombo.currentData()
        query = ("SELECT product_qouta FROM products WHERE product_id =?")
        qouta = cur.execute(query, (product_id,)).fetchone()
        
        for i in range(1, qouta[0] + 1):
            self.quantityCombo.addItem(str(i))

    def sellProduct(self):
        global productName, productId, memberName, memberId, quantity
        productName = self.productCombo.currentText()
        productId = self.productCombo.currentData()
        memberName=self.memberCombo.currentText()
        memberId=self.memberCombo.currentData()
        quantity = int(self.quantityCombo.currentText())
        self.confirm = ConfirmWindow()
        self.close()

class ConfirmWindow(QWidget):
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
        global productName, productId, memberName, memberId, quantity
        priceQuery = ("SELECT product_price FROM products WHERE product_id=?")
        price = cur.execute(priceQuery,(productId,)).fetchone()
        self.productName = QLabel()
        self.productName.setText(productName)
        self.memberName = QLabel()
        self.memberName.setText(memberName)
        self.amount = quantity * price[0]
        self.amountLabel = QLabel()
        self.amountLabel.setText(str(quantity) + "x" + str(price[0]) + "= R$" + str(self.amount))
        self.confirmBtn = QPushButton("Confirm")
        self.confirmBtn.clicked.connect(self.confirm)


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
        self.bottomLayout.addRow(QLabel("Product: "), self.productName)
        self.bottomLayout.addRow(QLabel("Member: "), self.memberName)
        self.bottomLayout.addRow(QLabel("Amount: "), self.amountLabel)
        self.bottomLayout.addRow(QLabel(""), self.confirmBtn)
        self.bottomFrame.setLayout(self.bottomLayout)

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.setLayout(self.mainLayout)

    def confirm(self):
        sellQuery = ("")