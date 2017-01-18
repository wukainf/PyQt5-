#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QSizePolicy, QLabel, QFontDialog


class Myform(QWidget):

    def __init__(self):

        super(Myform, self).__init__()
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)   # 固定按钮大小

        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Font 字体', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('fontdialog')
        self.show()

    def showDialog(self):

        font, ok = QFontDialog.getFont()    # FontPicker
        if ok:
            self.lbl.setFont(font)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())