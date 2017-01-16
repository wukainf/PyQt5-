#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class Myform(QMainWindow):
    def __init__(self):
        super(Myform, self).__init__()

        self.initUI()

    def initUI(self):

        self.statusBar()

        exitAction = QAction(QIcon('1.jpg'), '&Exit', self)     # 创建功能按钮
        # exitAction.setStatusTip('Exit application')
        exitAction.setShortcut('Ctrl+Q')       # 为功能按钮添加快捷键
        exitAction.triggered.connect(qApp.quit)       # 为功能按钮绑定事件

        menuBar = self.menuBar()      # 添加菜单栏
        QuitMenu = menuBar.addMenu('&Quit')   # 菜单栏中添加Quit菜单
        QuitMenu.addAction(exitAction)    # 在Quit菜单中添加功能按钮


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('menubar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())
