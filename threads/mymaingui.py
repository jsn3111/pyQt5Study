from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MyMainGUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.qtxt1 = QTextEdit(self)
        self.start_btn = QPushButton("Start", self)
        self.stop_btn  = QPushButton("Stop", self)
        self.addSec_btn   = QPushButton("Add 100", self)
        self.send_btn  = QPushButton("send instance", self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.qtxt1)
        vbox.addWidget(self.start_btn)
        vbox.addWidget(self.stop_btn)
        vbox.addWidget(self.addSec_btn)
        vbox.addWidget(self.send_btn)
        self.setLayout(vbox)

        self.setGeometry(100, 50, 300, 300)

