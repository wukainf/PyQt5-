#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtCore import QCoreApplication

class Myform(QWidget):
    def __init__(self):
        super(Myform, self).__init__()

        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        # 信号&槽机制: clicked是信号,quit是槽(事件),QCoreApplication.instance()是事件对象
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())
