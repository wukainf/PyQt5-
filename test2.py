#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Myform(QWidget):
        def __init__(self):
                #QWidget.__init__(self)
                super(Myform, self).__init__()
                #调用父类QWidget的构造函数,这句很重要
                self.setWindowTitle('hello world agian')
                self.resize(400, 300)

if __name__ == "__main__":
        app = QApplication(sys.argv)
        w = Myform()
        w.show()
        app.exec_()
