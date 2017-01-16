#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class Myform(QMainWindow):
    def __init__(self):
        super(Myform, self).__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('1.jpg'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        toolbar = self.addToolBar('Exit')   # 在窗体内添加包含一个名为Exit按钮的工具条
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 200, 150)
        self.setWindowTitle('toolbar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())



