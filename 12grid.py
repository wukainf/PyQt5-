#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication,QPushButton, QGridLayout

class Myform(QWidget):
    def __init__(self):
        super(Myform, self).__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        btns = ['存储', '取存', '退格', '清屏',
                '累存', '积存', '清存', '/',
                '7', '8', '9', '*',
                '4', '5', '6', '-',
                '1', '2', '3', '+',
                '0', '.', '+/-', '='
                ]

        positions = [(i, j) for i in range(6) for j in range(4)]

        for position, btn in zip(positions, btns):
            if btn == '':
                pass
            btn = QPushButton(btn)
            grid.addWidget(btn, position)




        #self.setGeometry(300, 300, 300, 200)
        self.move(300, 300)
        self.setWindowTitle('grid')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())

