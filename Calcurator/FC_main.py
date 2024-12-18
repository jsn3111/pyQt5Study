import sys
import time
import PyQt5

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

CalUi = './_uiFiles/calculator.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        uic.loadUi(CalUi, self)

        self.num_pushButton_1.clicked.connect(lambda state, button=self.num_pushButton_1: self.NumClicked(state, button))
        self.num_pushButton_2.clicked.connect(lambda state, button=self.num_pushButton_2: self.NumClicked(state, button))
        self.num_pushButton_3.clicked.connect(lambda state, button=self.num_pushButton_3: self.NumClicked(state, button))
        self.num_pushButton_4.clicked.connect(lambda state, button=self.num_pushButton_4: self.NumClicked(state, button))
        self.num_pushButton_5.clicked.connect(lambda state, button=self.num_pushButton_5: self.NumClicked(state, button))
        self.num_pushButton_6.clicked.connect(lambda state, button=self.num_pushButton_6: self.NumClicked(state, button))
        self.num_pushButton_7.clicked.connect(lambda state, button=self.num_pushButton_7: self.NumClicked(state, button))
        self.num_pushButton_8.clicked.connect(lambda state, button=self.num_pushButton_8: self.NumClicked(state, button))
        self.num_pushButton_9.clicked.connect(lambda state, button=self.num_pushButton_9: self.NumClicked(state, button))
        self.num_pushButton_0.clicked.connect(lambda state, button=self.num_pushButton_0: self.NumClicked(state, button))
        self.sign_pushButton_1.clicked.connect(lambda state, button=self.sign_pushButton_1: self.NumClicked(state, button))
        self.sign_pushButton_2.clicked.connect(lambda state, button=self.sign_pushButton_2: self.NumClicked(state, button))
        self.sign_pushButton_3.clicked.connect(lambda state, button=self.sign_pushButton_3: self.NumClicked(state, button))
        self.sign_pushButton_4.clicked.connect(lambda state, button=self.sign_pushButton_4: self.NumClicked(state, button))

        self.gualhoR_pushButton.clicked.connect(lambda state, button=self.gualhoR_pushButton: self.NumClicked(state, button))
        self.gualhoL_pushButton.clicked.connect(lambda state, button=self.gualhoL_pushButton: self.NumClicked(state, button))
        self.dot_pushButton.clicked.connect(lambda state, button=self.dot_pushButton: self.NumClicked(state, button))
        self.per_pushButton.clicked.connect(lambda state, button=self.per_pushButton: self.NumClicked(state, button))


        self.result_pushButton.clicked.connect(self.MakeResult)
        self.reset_pushButton.clicked.connect(self.Reset)
        self.del_pushButton.clicked.connect(self.Delete)

        self.del_pushButton.setStyleSheet('image:url(DelKey-2.png);')

    def Delete(self):
        exist_line_text = self.q_lineEdit.text()
        exist_line_text = exist_line_text[:-1]
        self.q_lineEdit.setText(exist_line_text)

    def Reset(self):
        self.q_lineEdit.clear()
        self.a_lineEdit.setText('0')

    def MakeResult(self):
        try:
            result = eval(self.q_lineEdit.text())
            self.a_lineEdit.setText(str(result))
        except Exception as e:
            print(e)

    def NumClicked(self, state, button):
        if button == self.per_pushButton:
            now_num_text = '*0.01'
        else:
            now_num_text = button.text()
        exist_line_text = self.q_lineEdit.text()
        self.q_lineEdit.setText(exist_line_text + now_num_text)

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()