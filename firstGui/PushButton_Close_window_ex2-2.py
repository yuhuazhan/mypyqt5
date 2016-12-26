# -*- coding: utf-8 -*-
import sys
import  time
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
        self.button2 = QPushButton(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height) #設定窗口尺寸
        self.label1.setText('okkkkk')
        self.label1.move(20,20)
        self.label2.setText('94v0i1c1k3y')
        self.label2.move(20,40)
        self.button1.setText('test')
        self.button1.move(100,80)
        self.button2.move(0,80)
        self.button2.setText('close')
        #clicked是按鈕的signal
        self.button1.clicked.connect(self.buttonClicked) #連接signal 和slot
        self.button2.clicked.connect(self.buttonClicked2)
        self.show()
    #按鈕點擊事件(slot)
    def buttonClicked(self):
        self.label1.setText('change by click test')
    def buttonClicked2(self):
        print('close by click close button')
        self.close(self)
    def closeEvent(self, event):
        print("User has clicked the red x on the main window")
if __name__  == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())