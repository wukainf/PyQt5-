#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt


class Myform(QWidget):

    def __init__(self):

        super(Myform, self).__init__()

        self.initUI()

    def initUI(self):

        cb = QCheckBox('show title', self)
        cb.move(20, 20)
        cb.toggle()    # 切换默认状态为选中

        # 当进行如下设置时,state会有三个值(0,1,2)
        # cb.setCheckState(1)

        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('checkbox')
        self.show()

    # stateChanged信号会传入一个状态参数(默认0和2)
    def changeTitle(self, state):

        # print state

        if state == Qt.Checked:
           self.setWindowTitle('checkbox')
        else:
           self.setWindowTitle('')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())