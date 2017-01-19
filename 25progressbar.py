#! usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
from PyQt5.QtCore import QBasicTimer


class Myform(QWidget):

    def __init__(self):

        super(Myform, self).__init__()

        self.initUI()

    def initUI(self):

        # 这是两个自定义的中间变量,后面会用到
        self.finish = 0
        self.beginAgain = 0

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('progressbar')
        self.show()

    def doAction(self):

        source = self.sender()

        # 进度条到100%时触发,点击时将中间变量self.beginAgain置为1
        if self.finish == 1:
            self.timer.start(100, self)
            self.btn.setText('Stop')
            self.beginAgain = 1

        elif self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')

        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')

    def timerEvent(self, e, s = 0):

        if self.step >= 100:

            if self.beginAgain == 0:
                self.timer.stop()
                self.btn.setText('BeginAgain')
                self.finish = 1

            # 进度条到100%并且点击按钮触发
            elif self.beginAgain == 1:
                self.step = 0
                self.beginAgain = 0

        else:
            self.finish = 0

        self.step = self.step + 1
        self.pbar.setValue(self.step)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())