#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QToolTip, QPushButton
from PyQt5.QtGui import QFont

class Myform(QWidget):
    def __init__(self):
        super(Myform, self).__init__()

        self.initUI()


    def initUI(self):
        #QToolTip.setFont(QFont('SansSerif', 20))

        self.setToolTip('This is a <b>QWidget</b> widget')      #设置窗口的提示内容

        btn = QPushButton('Button', self)    # 按钮组件
        btn.setToolTip('This is a <b>QPushButton</b> widget')      # 设置按钮的提示内容
        btn.resize(btn.sizeHint())  # 设置组件为推荐大小

        btn.move(0,0)       # 从内容开始移位

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('tips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())