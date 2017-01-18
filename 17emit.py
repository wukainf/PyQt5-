#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, QObject

# 定义新事件类
class Communicate(QObject):

    closeApp = pyqtSignal()

class Myform(QMainWindow):

    def __init__(self):

        super(Myform, self).__init__()
        self.initUI()

    def initUI(self):

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.move(300, 300)
        self.resize(300, 200)
        self.setWindowTitle('emitsignal')
        self.show()

    # 事件传递
    def mousePressEvent(self, event):

        self.c.closeApp.emit()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())

