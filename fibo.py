import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ctypes import cdll

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)

test = cdll.LoadLibrary('fibo.dll')
print(test.fibo(10))

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec()

