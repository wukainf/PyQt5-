#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class Myform(QWidget):
    def __init__(self):
        super(Myform, self).__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        article = QLabel('Article')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        articleEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)   # 设置组件间的距离

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(article, 3, 0)
        grid.addWidget(articleEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.move(300, 300)
        self.setWindowTitle('layout')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())