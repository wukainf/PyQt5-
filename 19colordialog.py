#! /usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog
from PyQt5.QtGui import QColor

class Myform(QWidget):

    def __init__(self):

        super(Myform, self).__init__()
        self.initUI()

    def initUI(self):

        col = QColor(100, 100, 123)

        self.btn = QPushButton('dialog', self)
        self.btn.move(100, 100)

        self.btn.clicked.connect(self.showDialog)

        # 初始化QFrame的颜色
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget {background-color: %s}" % col.name())

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('colordialog')
        self.show()

    def showDialog(self):

        col = QColorDialog.getColor()    # ColorPicker

        if col.isValid():   # 当点击Ok时col.isValid()为True,点击Cancel或关闭为False

            self.frm.setStyleSheet("QWidget { background-color: %s}" % col.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())