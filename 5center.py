#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget

class Myform(QWidget):
    def __init__(self):
        super(Myform, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 300)
        self.center()
        self.setWindowTitle('居中对齐')

        self.show()

    def center(self):
        qr = self.frameGeometry()        # 获得窗口框架
        cp = QDesktopWidget().availableGeometry().center()     # 得到屏幕尺寸的中心位置
        qr.moveCenter(cp)    #将框架的中心点移到之前获得的中心位置
        self.move(qr.topLeft())      #将窗口移动到框架位置

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())

