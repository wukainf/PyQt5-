#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame
from PyQt5.QtGui import QColor


class Myform(QWidget):

    def __init__(self):

        super(Myform, self).__init__()

        self.initUI()

    def initUI(self):

        self.col = QColor(0, 0, 0)

        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)
        # 这是一个独立的事件, 点击传递一个bool值并触发事件
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)
        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)
        blueb.clicked[bool].connect(self.setColor)


        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('togglebutton')
        self.show()

    def setColor(self, pressed):

        source = self.sender()   # 事件发送者名

        if pressed:
            val = 255
        else: val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        elif source.text() == "Blue":
            self.col.setBlue(val)
        else:
            print "未知错误"

        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())
