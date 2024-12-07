from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Worker(QThread):
    sec_changed = pyqtSignal(str)

    def __init__(self, sec=0, parent=None):
        super().__init__()
        self.main = parent
        self.working = True
        self.sec = sec

    def __del__(self):
        print(".... end thread ....")
        self.wait()

    def run(self):
        while self.working:
            self.sec_changed.emit('time (secs) : {}'.format(self.sec))
            self.sleep(1)
            self.sec += 1

    @pyqtSlot()
    def add_sec(self):
        print("add_sec ....")
        self.sec += 100

    @pyqtSlot("PyQt_PyObject")
    def receive_instance_signal(self, inst):
        print(inst.name)

