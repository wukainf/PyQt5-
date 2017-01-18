#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QInputDialog, QPushButton

class Myform(QWidget):

    def __init__(self):

        super(Myform, self).__init__()
        self.initUI()

    def initUI(self):

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 20)

        self.move(300, 300)
        self.resize(300, 200)
        self.setWindowTitle('dialog')
        self.show()

    def showDialog(self):

        # 返回值:文本内容和一个布尔值,参数:self, 对话框标题, 提示内容
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text.encode('utf-8')))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())