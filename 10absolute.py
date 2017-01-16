#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel

class Myform(QWidget):
    def __init__(self):
        super(Myform, self).__init__()
        self.initUI()

    def initUI(self):
        l1 = QLabel('l1', self)
        l1.move(0, 0)

        l2 = QLabel('l2', self)
        l2.move(40, 40)

        l3 = QLabel('l3', self)
        l3.move(80, 80)

        self.setGeometry(300, 200, 200, 150)
        self.setWindowTitle('absolute position')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())