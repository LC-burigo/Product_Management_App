import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

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
        self.layout()

    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        #####################Toolbar Buttons########################
        #####################Add Product############################
        self.addProduct = QAction(QIcon('icons/add.png'), "Add Product", self)
        self.tb.addAction(self.addProduct)
        self.tb.addSeparator()
        ###########################add Member######################
        self.addMember = QAction(QIcon('icons/users.png'), "Add Member", self)
        self.tb.addAction(self.addMember)
        self.tb.addSeparator()
        ########################Sell Products#########################
        self.sellProduct = QAction(QIcon('icons/sell.png'), "Sell Product", self)
        self.tb.addAction(self.sellProduct)
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
        #########################Product table widget###############
        self.productsTable = QTableWidget()
        self.productsTable.setColumnCount(6)
        self.productsTable.setColumnHidden(0, True)
        self.productsTable.setHorizontalHeaderItem(0, QTableWidgetItem("Product ID"))
        self.productsTable.setHorizontalHeaderItem(1, QTableWidgetItem("Product Name"))
        self.productsTable.setHorizontalHeaderItem(2, QTableWidgetItem("Manufacturer"))
        self.productsTable.setHorizontalHeaderItem(3, QTableWidgetItem("Price"))
        self.productsTable.setHorizontalHeaderItem(4, QTableWidgetItem("Quota"))
        self.productsTable.setHorizontalHeaderItem(5, QTableWidgetItem("Availbility"))

    def layouts(self):
        ######################Tabl Layouts##################
        self.mainLayout = QHBoxLayout()
        self.mainLeftLayout = QVBoxLayout()
        self.mainRightLayout = QVBoxLayout()
        self.RightTopLayout = QHBoxLayout()
        self.RightMiddleLayout = QHBoxLayout()
        self.topGroupBox = QGroupBox()
        self.middleGroupBox = QGroupBox()

        self.mainLeftLayout.addWidget(self.productsTable)
        self.mainLayout.addLayout(self.mainLeftLayout)
        self.tab1.setLayout(self.mainLayout)


def main():
    App=QApplication(sys.argv)
    window=Main()
    sys.exit(App.exec_())

if __name__== '__main__':
    main()
