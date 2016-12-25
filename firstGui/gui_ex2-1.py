# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QLabel
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title  = 'PyQt App'
        self.left  = 250
        self.top  = 250
        self.width  = 800
        self.height = 600

        self.label1  = QLabel(self)
        self.label2  = QLabel(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height) #設定窗口尺寸
        self.statusBar().showMessage('hello')
        self.label1.setText('okkkkk')

        self.label1.move(20,20)
        self.label2.move(60,80)

        answer = QMessageBox.question(self,'test','pollw',QMessageBox.No|QMessageBox.Yes)
        if answer == QMessageBox.Yes:
            self.show()
        elif answer == QMessageBox.No:
            print('no')

if __name__  == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())