# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title  = 'PyQt App'
        self.left  = 250
        self.top  = 250
        self.width  = 400
        self.height = 300

        self.label1  = QLabel(self)
        self.label2  = QLabel(self)
        self.button1 = QPushButton(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height) #設定窗口尺寸
        self.label1.setText('okkkkk')
        self.label1.move(20,20)
        self.label2.setText('94v0i1c1k3y')
        self.label2.move(20,40)
        self.button1.setText('test')
        self.button1.move(20,80)
        #clicked是按鈕的signal
        self.button1.clicked.connect(self.buttonClicked) #連接signal 和slot
        self.show()
    #按鈕點擊事件(slot)
    def buttonClicked(self):
        self.label1.setText('xxxxx')

if __name__  == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())