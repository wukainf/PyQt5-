#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Myform(QMainWindow):
    def __init__(self):
        super(Myform, self).__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')    # 创建状态栏
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('status bar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())

