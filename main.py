import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import addproduct, addmember, sellings
from PIL import Image

con = sqlite3.connect("products.db")
cur = con.cursor()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Manager")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 1350, 750)
        self.setFixedSize(self.size())

        self.UI()
        self.show()

    def UI(self):
        self.toolBar()
        self.tabWigdet()
        self.widgets()
        self.layouts()
        self.displayProducts()
        self.displayMembers()

    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        #####################Toolbar Buttons########################
        #####################Add Product############################
        self.addProduct = QAction(QIcon('icons/add.png'), "Add Product", self)
        self.tb.addAction(self.addProduct)
        self.addProduct.triggered.connect(self.funcAddProduct)
        self.tb.addSeparator()
        ###########################add Member######################
        self.addMember = QAction(QIcon('icons/users.png'), "Add Member", self)
        self.tb.addAction(self.addMember)
        self.addMember.triggered.connect(self.funcAddMember)
        self.tb.addSeparator()
        ########################Sell Products#########################
        self.sellProduct = QAction(QIcon('icons/sell.png'), "Sell Product", self)
        self.tb.addAction(self.sellProduct)
        self.sellProduct.triggered.connect(self.funcSellProducts)
        self.tb.addSeparator()

    def tabWigdet(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab1, "Products")
        self.tabs.addTab(self.tab2, "Members")
        self.tabs.addTab(self.tab3, "Statistics")

    def widgets(self):
        #########################tab1 widgets#######################
        #########################Main left layout widget############
        self.productsTable = QTableWidget()
        self.productsTable.setColumnCount(6)
        self.productsTable.setColumnHidden(0, True)
        self.productsTable.setHorizontalHeaderItem(0, QTableWidgetItem("Product ID"))
        self.productsTable.setHorizontalHeaderItem(1, QTableWidgetItem("Product Name"))
        self.productsTable.setHorizontalHeaderItem(2, QTableWidgetItem("Manufacturer"))
        self.productsTable.setHorizontalHeaderItem(3, QTableWidgetItem("Price"))
        self.productsTable.setHorizontalHeaderItem(4, QTableWidgetItem("Quota"))
        self.productsTable.setHorizontalHeaderItem(5, QTableWidgetItem("Availability"))
        self.productsTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.productsTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.productsTable.doubleClicked.connect(self.selectedProduct)
        #########################right top layout widget#############
        self.searchText = QLabel("Search")
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText("Search For Products")
        self.searchButton = QPushButton("Search")
        self.searchButton.clicked.connect(self.searchProducts)
        #########################right middle layout widget#############
        self.allProducts = QRadioButton("All Products")
        self.availableProducts = QRadioButton("Available Products")
        self.notAvailablealProducts = QRadioButton(" Not Available Products")
        self.listButton = QPushButton("List")
        self.listButton.clicked.connect(self.listProducts)
        #########################tab2 widgets#######################
        self.membersTable = QTableWidget()
        self.membersTable.setColumnCount(4)
        self.membersTable.setHorizontalHeaderItem(0, QTableWidgetItem("Member ID"))
        self.membersTable.setHorizontalHeaderItem(1, QTableWidgetItem("Member Name"))
        self.membersTable.setHorizontalHeaderItem(2, QTableWidgetItem("Member Surname"))
        self.membersTable.setHorizontalHeaderItem(3, QTableWidgetItem("Phone"))
        self.membersTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.membersTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.membersTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.membersTable.doubleClicked.connect(self.selectedMember)
        self.memberSearchText = QLabel("Search Members")
        self.memberSearchEntry = QLineEdit()
        self.memberSearchButton = QPushButton("Search")
        self.memberSearchButton.clicked.connect(self.searchMembers)

    def layouts(self):
        ######################Tabl Layouts##################
        self.mainLayout = QHBoxLayout()
        self.mainLeftLayout = QVBoxLayout()
        self.mainRightLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightMiddleLayout = QHBoxLayout()
        self.topGroupBox = QGroupBox("Search Box")
        self.middleGroupBox = QGroupBox("List Box")
        ######################Add  Widgets##################
        ######################Left main layout widgets##################
        self.mainLeftLayout.addWidget(self.productsTable)
        ######################Right main layout widgets##################
        self.rightTopLayout.addWidget(self.searchText)
        self.rightTopLayout.addWidget(self.searchEntry)
        self.rightTopLayout.addWidget(self.searchButton)
        self.topGroupBox.setLayout(self.rightTopLayout)
        ######################Right middle layout widgets##################
        self.rightMiddleLayout.addWidget(self.allProducts)
        self.rightMiddleLayout.addWidget(self.availableProducts)
        self.rightMiddleLayout.addWidget(self.notAvailablealProducts)
        self.rightMiddleLayout.addWidget(self.listButton)
        self.middleGroupBox.setLayout(self.rightMiddleLayout)

        self.mainRightLayout.addWidget(self.topGroupBox)
        self.mainRightLayout.addWidget(self.middleGroupBox)
        self.mainLayout.addLayout(self.mainLeftLayout, 70)
        self.mainLayout.addLayout(self.mainRightLayout, 30)
        self.tab1.setLayout(self.mainLayout)
        ######################Tabl2 Layouts##################
        self.memberMainLayout = QHBoxLayout()
        self.memberLeftLayout = QHBoxLayout()
        self.memberRightLayout = QHBoxLayout()
        self.memberRightGroupBox = QGroupBox("Search For Members")
        self.memberRightGroupBox.setContentsMargins(10, 10, 10, 600)

        self.memberRightLayout.addWidget(self.memberSearchText)
        self.memberRightLayout.addWidget(self.memberSearchEntry)
        self.memberRightLayout.addWidget(self.memberSearchButton)
        self.memberRightGroupBox.setLayout(self.memberRightLayout)

        self.memberLeftLayout.addWidget(self.membersTable)
        self.memberMainLayout.addLayout(self.memberLeftLayout, 70)
        self.memberMainLayout.addWidget(self.memberRightGroupBox, 30)
        self.tab2.setLayout(self.memberMainLayout)

    def funcAddProduct(self):
        self.newProduct = addproduct.AddProduct()

    def funcAddMember(self):
        self.newMember = addmember.AddMember()

    def displayProducts(self):
        self.productsTable.setFont(QFont("Times", 12))
        for i in reversed(range(self.productsTable.rowCount())):
            self.productsTable.removeRow(i)

        query = cur.execute("SELECT product_id, product_name, product_manufacterer, product_price, product_qouta, product_availability FROM products")

        for row_data in query:
            row_number = self.productsTable.rowCount()
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def displayMembers(self):
        self.membersTable.setFont(QFont("Times", 12))
        for i in reversed(range(self.membersTable.rowCount())):
            self.membersTable.removeRow(i)

        query = cur.execute("SELECT * FROM members")

        for row_data in query:
            row_number = self.membersTable.rowCount()
            self.membersTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.membersTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.membersTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def selectedProduct(self):
        global productId
        listProduct = []
        for i in range(0, 6):
            listProduct.append(self.productsTable.item(self.productsTable.currentRow(), i).text())
        
        productId = listProduct[0]
        self.display = displayProduct()
        self.display.show()

    def selectedMember(self):
        global memberId
        listMember = []
        for i in range(0, 4):
            listMember.append(self.membersTable.item(self.membersTable.currentRow(), i).text())

        memberId = listMember[0]
        self.displayMember = displayMember()
        self.displayMember.show()

    def searchProducts(self):
        value = self.searchEntry.text()
        if value == "":
            QMessageBox.information(self, "Warning", "Search Query cant be empty!!!")
        else:
            self.searchEntry.setText("")

            query = "SELECT product_id, product_name, product_manufacterer, product_price, product_qouta, product_availability FROM products WHERE product_name LIKE ? or product_manufacterer LIKE ?"
            results = cur.execute(query, ('%'+value+'%','%'+value+'%')).fetchall()
        
            if results == []:
                QMessageBox.information(self, "Warning", "There is no such a product or manufacturer")
            else:
                for i in reversed(range(self.productsTable.rowCount())):
                    self.productsTable.removeRow(i)
                
                for row_data in results:
                    row_number = self.productsTable.rowCount()
                    self.productsTable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    
    def searchMembers(self):
        value = self.memberSearchEntry.text()
        if value == "":
            QMessageBox.information(self, "Warning", "Search Query cant be empty!!!")
        else:
            self.memberSearchEntry.setText("")

            query = "SELECT * FROM members WHERE member_name LIKE ? or member_surname LIKE ? or member_phone LIKE ?"
            results = cur.execute(query, ('%'+value+'%','%'+value+'%', '%'+value+'%')).fetchall()
        
            if results == []:
                QMessageBox.information(self, "Warning", "There is no such a member")
            else:
                for i in reversed(range(self.membersTable.rowCount())):
                    self.membersTable.removeRow(i)
                
                for row_data in results:
                    row_number = self.membersTable.rowCount()
                    self.membersTable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.membersTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def listProducts(self):
        if self.allProducts.isChecked() == True:
            self.displayProducts()
        elif self.availableProducts.isChecked() == True:
            query = ("SELECT product_id, product_name, product_manufacterer, product_price, product_qouta, product_availability FROM products WHERE product_availability = 'Available'")
            products = cur.execute(query).fetchall()

            for i in reversed(range(self.productsTable.rowCount())):
                    self.productsTable.removeRow(i)

            for row_data in products:
                    row_number = self.productsTable.rowCount()
                    self.productsTable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        elif self.notAvailablealProducts.isChecked() == True:
            query = ("SELECT product_id, product_name, product_manufacterer, product_price, product_qouta, product_availability FROM products WHERE product_availability = 'Unavailable'")
            products = cur.execute(query).fetchall()

            for i in reversed(range(self.productsTable.rowCount())):
                    self.productsTable.removeRow(i)

            for row_data in products:
                    row_number = self.productsTable.rowCount()
                    self.productsTable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def funcSellProducts(self):
        self.sellProduct = sellings.SellProducts()

class displayProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Details")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 350, 600)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.product_Details()
        self.widgets()
        self.layouts()

    def product_Details(self):
        global productId
        query = ("SELECT * FROM products WHERE product_id=?")
        product = cur.execute(query, (productId,)).fetchone()
        self.product_Name = product[1]
        self.product_Manufacterer = product[2]
        self.product_Price = product[3]
        self.product_Qouta = product[4]
        self.productImg = product[5]
        self.productStatus = product[6]
    
    def widgets(self):
        ########################Top layout widgets##################
        self.product_Img = QLabel()
        self.img = QPixmap('img/{}'.format(self.productImg))
        self.product_Img.setPixmap(self.img)
        self.product_Img.setAlignment(Qt.AlignCenter)
        self.titleText = QLabel("Display Product")
        self.titleText.setAlignment(Qt.AlignCenter)
        ########################Bottom layout widgets##################
        self.nameEntry = QLineEdit()
        self.nameEntry.setText(self.product_Name)
        self.manufacturerEntry = QLineEdit()
        self.manufacturerEntry.setText(self.product_Manufacterer)
        self.priceEntry = QLineEdit()
        self.priceEntry.setText(str(self.product_Price))
        self.qoutaEntry = QLineEdit()
        self.qoutaEntry.setText(str(self.product_Qouta))
        self.availabilityCombo = QComboBox()
        self.availabilityCombo.addItems(["Available", "Unavailable"])
        self.uploadBtn = QPushButton("Upload")
        self.uploadBtn.clicked.connect(self.uploadImg)
        self.deleteBtn = QPushButton("Delete")
        self.deleteBtn.clicked.connect(self.deleteproduct)
        self.updateBtn = QPushButton("Update")
        self.updateBtn.clicked.connect(self.updateProduct)

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.bottomFrame = QFrame()
        ####################add widgets#######################
        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.product_Img)
        self.topFrame.setLayout(self.topLayout)

        self.bottomLayout.addRow(QLabel("Name: "), self.nameEntry)
        self.bottomLayout.addRow(QLabel("Manufacturer: "), self.manufacturerEntry)
        self.bottomLayout.addRow(QLabel("Price: "), self.priceEntry)
        self.bottomLayout.addRow(QLabel("Qouta: "), self.qoutaEntry)
        self.bottomLayout.addRow(QLabel("Status"), self.availabilityCombo)
        self.bottomLayout.addRow(QLabel("Image: "), self.uploadBtn)
        self.bottomLayout.addRow(QLabel(""), self.deleteBtn)
        self.bottomLayout.addRow(QLabel(""), self.updateBtn)
        self.bottomFrame.setLayout(self.bottomLayout)

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.setLayout(self.mainLayout)

    def uploadImg(self):
        size = (256, 256)
        self.filename, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image files (*.jpg *.png)')
        if ok:
            self.productImg = os.path.basename(self.filename)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save("img/{0}".format(self.productImg))

    def updateProduct(self):
        global productId
        name = self.nameEntry.text()
        manufacturer = self.manufacturerEntry.text()
        price = int(self.priceEntry.text())
        qouta = int(self.qoutaEntry.text())
        status = self.availabilityCombo.currentText()
        defaultImg = self.productImg

        if (name and manufacturer and price and qouta !=""):

            try:
                query = "UPDATE products set product_name=?, product_manufacterer=?, product_price=?, product_qouta=?, product_img=?, product_availability=? WHERE product_id=?"
                cur.execute(query, (name, manufacturer, price, qouta, defaultImg, status, productId))
                con.commit()
                QMessageBox.information(self, "Info", "Product has been updated!")
            except:
                QMessageBox.information(self, "Info", "Product hasnt been updated")
        else:
            QMessageBox.information(self, "Info", "Fields cant be empty!!!")

    def deleteproduct(self):
        global productId

        mbox = QMessageBox.question(self, "Warning", "Are you sure to delete this product?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                cur.execute("DELETE FROM products WHERE product_id=?", (productId,))
                con.commit()
                QMessageBox.information(self, "Information", "Product has been deleted!")
                self.close()
            except:
                QMessageBox.information(
                    self, "Information", "Product hasnt been deleted!")
        

class displayMember(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Members Details")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 350, 600)
        self.setFixedSize(self.size())
        self.UI()
        self.show()
    
    def UI(self):
        self.member_Details()
        self.widgets()
        self.layout()

    def member_Details(self):
        global memberId
        query = ("SELECT * FROM members WHERE member_id=?")
        member = cur.execute(query, (memberId,)).fetchone()
        self.member_Name = member[1]
        self.member_Surname = member[2]
        self.member_Phone = member[3]

    def widgets(self):
        ########################Top layout widgets##################
        self.member_Img = QLabel()
        self.img = QPixmap('icons/members.png')
        self.member_Img.setPixmap(self.img)
        self.member_Img.setAlignment(Qt.AlignCenter)
        self.titleText = QLabel("Display Member")
        self.titleText.setAlignment(Qt.AlignCenter)
        ########################Bottom layout widgets##################
        self.nameEntry = QLineEdit()
        self.nameEntry.setText(self.member_Name)
        self.surnameEntry = QLineEdit()
        self.surnameEntry.setText(self.member_Surname)
        self.phoneEntry = QLineEdit()
        self.phoneEntry.setText(str(self.member_Phone))
        self.deleteBtn = QPushButton("Delete")
        self.deleteBtn.clicked.connect(self.deletemember)
        self.updateBtn = QPushButton("Update")
        self.updateBtn.clicked.connect(self.updatemember)

    def layout(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.bottomFrame = QFrame()
        ####################add widgets#######################
        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.member_Img)
        self.topFrame.setLayout(self.topLayout)

        self.bottomLayout.addRow(QLabel("Name: "), self.nameEntry)
        self.bottomLayout.addRow(QLabel("Surname: "), self.surnameEntry)
        self.bottomLayout.addRow(QLabel("Phone: "), self.phoneEntry)
        self.bottomLayout.addRow(QLabel(""), self.updateBtn)
        self.bottomLayout.addRow(QLabel(""), self.deleteBtn)
        self.bottomFrame.setLayout(self.bottomLayout)

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.setLayout(self.mainLayout)

    def updatemember(self):
        global memberId
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()

        if (name and surname and phone !=""):

            try:
                query = "UPDATE members set member_name=?, member_surname=?, member_phone=? WHERE member_id=?"
                cur.execute(query, (name, surname, phone, memberId))
                con.commit()
                QMessageBox.information(self, "Info", "Member has been updated!")
            except:
                QMessageBox.information(
                    self, "Info", "Member hasnt been updated")
        else:
            QMessageBox.information(self, "Info", "Fields cant be empty!!!")
    
    def deletemember(self):
        global memberId

        mbox = QMessageBox.question(self, "Warning", "Are you sure to delete this member?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                cur.execute("DELETE FROM members WHERE member_id=?", (memberId,))
                con.commit()
                QMessageBox.information(self, "Information", "Product has been deleted!")
                self.close()
            except:
                QMessageBox.information(self, "Information", "Product hasnt been deleted!")


def main():
    App=QApplication(sys.argv)
    window=Main()
    sys.exit(App.exec_())

if __name__== '__main__':
    main()
