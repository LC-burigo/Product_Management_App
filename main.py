import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

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

    def toolBar(self):
        self.tb=self.addToolBar("Tool Bar")
        self.addProduct = QAction(QIcon('icons/add.png'), "Add Product", self)
        self.tb.addAction(self.addProduct)

def main():
    App=QApplication(sys.argv)
    window=Main()
    sys.exit(App.exec_())

if __name__== '__main__':
    main()