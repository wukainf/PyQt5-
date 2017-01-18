#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt

class Myform(QWidget):

    def __init__(self):

        super(Myform, self).__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('reimplement')
        self.show()

    # 重写了KeyPressEvent事件函数
    def keyPressEvent(self, e):

        # 当按下键盘上的'q'时,程序退出
        if e.key() == Qt.Key_Q:
            self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())