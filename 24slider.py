#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


class Myform(QMainWindow):

    def __init__(self):

        super(Myform, self).__init__()

        self.initUI()

    def initUI(self):

        self.col = QColor(0, 0, 0)

        self.sldr = QSlider(Qt.Horizontal, self)    # 创建一个横置的滑动条
        self.sldr.setFocusPolicy(Qt.NoFocus)
        self.sldr.setGeometry(30, 10, 100, 30)
        self.sldr.valueChanged[int].connect(self.changValue)
        self.sldr.setStatusTip('Red')

        self.lbr = QLabel(self)
        self.lbr.setGeometry(140, 10, 100, 30)


        self.sldg = QSlider(Qt.Horizontal, self)
        self.sldg.setFocusPolicy(Qt.NoFocus)
        self.sldg.setGeometry(30, 60, 100, 30)
        self.sldg.valueChanged[int].connect(self.changValue)
        self.sldg.setStatusTip('Green')

        self.lbg = QLabel(self)
        self.lbg.setGeometry(140, 60, 100, 30)


        self.sldb = QSlider(Qt.Horizontal, self)
        self.sldb.setFocusPolicy(Qt.NoFocus)
        self.sldb.setGeometry(30, 110, 100, 30)
        self.sldb.valueChanged[int].connect(self.changValue)
        self.sldb.setStatusTip('Blue')

        self.lbb = QLabel(self)
        self.lbb.setGeometry(140, 110, 100, 30)


        self.square = QFrame(self)
        self.square.setGeometry(180, 20, 100, 100)
        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('slider')
        self.show()

        self.statusBar()

    def changValue(self, val):

        if self.sender() == self.sldr:
            self.lbr.setText(str(val * 255 / 99))    # 将99刻度转换成255刻度
            self.col.setRed(val * 255/ 99)
        elif self.sender() == self.sldg:
            self.lbg.setText(str(val * 255 / 99))
            self.col.setGreen(val * 255/ 99)
        elif self.sender() == self.sldb:
            self.lbb.setText(str(val * 255 / 99))
            self.col.setBlue(val * 255/ 99)
        else: print "未知错误"

        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())

        self.statusBar().showMessage(self.col.name())   # 当颜色改变将颜色名写到状态栏
        self.square.setStatusTip(self.col.name())




if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())
