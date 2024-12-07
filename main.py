import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainGui(QDialog):
    def __init__(self):
        self.qtxt1 = QTextEdit(self)
        self.start_btn = QPushButton("Start", self)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.qtxt1)
        vbox.addWidget(self.start_btn)
        self.setLayout(vbox)
        self.setGeometry(100,50,300,300)
        
class Main(MainGui):
    def __init__(self, parent=None):
        super().__init__(parent)
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    form = Main()
    app.exec_()
    
    