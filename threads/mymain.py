from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#import Worker
#import mymaingui
class Worker(QThread):
	sec_changed = pyqtSignal(str)

	def __init__(self, sec=0, parent=None):
		super().__init__()
		self.main = parent
		self.working = True
		self.sec = sec
	def __del__(self):
		print("... end thread ....")
		self.wait()
	def run(self):
		while self.working == True:
			self.sec_changed.emit('time (sec) : {}'.format(self.sec))
			self.sleep(1)
			self.sec += 1
	@pyqtSlot()
	def add_sec(self):
		print("add_sec ....")
		self.sec += 100
	@pyqtSlot("PyQt_PyObject")
	def receive_instance_signal(self, inst):
		print(inst.name)

class MyMainGUI(QDialog):
    self.qtxt1 = QTextEdit(self)
    self.start_btn = QPushButton("Start", self)
    self.stop_btn = QPushButton("Stop", self)
    self.addSec_btn = QPushButton("Add 100", self)
    self.send_btn = QPushButton("send instance", self)

    vbox = QVBoxLayout()
    vbox.addWidget(self.qtxt1)
    vbox.addWidget(self.start_btn)
    vbox.addWidget(self.stop_btn)
    vbox.addWidget(self.addSec_btn)
    vbox.addWidget(self.send_btn)
    self.setLayout(vbox)
    self.setGeometry(100,50,300,300)

class Test:
    def __init__(self):
        name = ""

class MyMain(MyMainGUI):
    add_sec_signal = pyqtSignal()
    send_instance_signal = pyqtSignal("PyQt_PyObject")

    def __init__(self, parent=None):
        super().__init__(parent)

        self.start_btn.clicked.connect(self.time_start)
        self.stop_btn.clicked.connect(self.time_stop)
        self.addSec_btn.clicked.connect(self.add_sec)
        self.send_btn.clicked.connect(self.send_instance)

        self.th = Worker(parent=self)
        self.th.sec_changed.connect(self.time_update)  #'''custom signal from worker thread to main thread'''
        self.add_sec_signal.connect(self.th.add_sec)   #'''custom signal from main thread to worker thread'''
        self.send_instance.signal.connect(self.th.recieve_instance_signal)
        self.show()

    @pyqtSlot()
    def time_start(self):
        self.th.start()
        self.th.working = True

    @pyqtSlot()
    def time_stop(self):
        self.th.working = False

    @pyqtSlot()
    def add_sec(self):
        print(".... add signal emit....")
        self.add_sec_signal.emit()

    @pyqtSlot(str)
    def time_update(self, msg):
        self.qtxt1.append(msg)

    @pyqtSlot()
    def send_instance(self):
        t1 = Test()
        t1.name = "Super Power!!!"
        self.send_instance_signal.emit(t1)

if __name__=="__main__":
    import sys
    app = QAppliction(sys.argv)
    form = MyMain()
    app.exec_()

