#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout


class Myform(QMainWindow):

    def __init__(self):

        super(Myform, self).__init__()
        self.initUI()

    def initUI(self):

        btn1 = QPushButton('Button1', self)
        btn2 = QPushButton('Button2', self)

        # 为按钮添加点击事件
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)       # QMainWindow有自己的布局了,所以不能直接setLayout


        self.resize(300, 200)
        self.move(300, 300)
        self.setWindowTitle('sender')
        self.show()

        self.statusBar()

    def buttonClicked(self):

        # 事件: 显示信号发出者
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())
