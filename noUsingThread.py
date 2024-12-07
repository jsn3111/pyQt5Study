# Example not used thread
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import sys

class MainWidget(QWidget):
	def __init__(self):
		super().__init__()
		thread_start = QPushButton("Start")
		thread_start.clicked.connect(self.increaseNumber)

		vbox = QVBoxLayout()
		vbox.addWidget(thread_start)

		self.resize(200, 200)
		self.setLayout(vbox)

	# Function that increase by number 1 with pushing button
	def increaseNumber(self):
		for i in range(10):
			print("Thread:", i)
			time.sleep(1)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	widget = MainWidget()
	widget.show()
	sys.exit(app.exec())
