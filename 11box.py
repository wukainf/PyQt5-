#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout

class Myform(QWidget):
    def __init__(self):
        super(Myform, self).__init__()
        self.initUI()

    def initUI(self):
        ok = QPushButton('OK')
        cancel = QPushButton('Cancel')

        # 创建一个水平布局
        hbox = QHBoxLayout()
        hbox.addStretch(1)  # 拉伸因子,会占据多余空间
        hbox.addWidget(ok)
        hbox.addWidget(cancel)

        # 创建一个垂直布局
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        # 将水平布局放到垂直布局里
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('box')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())
