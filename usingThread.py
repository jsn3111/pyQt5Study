import sys
import time
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from ctypes import cdll

CalUI = './_uiFiles/calculator.ui'

increaseDef = cdll.LoadLibrary('increasePrint2.dll')

class Thread1(QThread):
	#parent = MainWidget inherient
	def __init__(self, parent):
		super().__init__(parent)
	def run(self):
		#for i in range(10):
		#	print("Thread : ", i)
		increaseDef.increasNum(500000)
		time.sleep(1)

class MainWidget(QWidget):
	def __init__(self):
		super().__init__()
		QDialog.__init__(self, None)
		uic.loadUi(CalUI, self)
		thread_start = QPushButton("START!")
		thread_start.clicked.connect(self.increaseNumber)

		vbox = QVBoxLayout()
		vbox.addWidget(thread_start)

		self.resize(200,200)
		self.setLayout(vbox)

	def increaseNumber(self):
		x = Thread1(self)
		x.start()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	widget = MainWidget()
	widget.show()
	sys.exit(app.exec())