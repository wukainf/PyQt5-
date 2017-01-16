#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Myform(QWidget):
    def __init__(self):
        super(Myform, self).__init__()

        self.initUI()

    def initUI(self):
        # 前两个参数定位了窗口x轴,y轴的位置,效果等同于self.move(300, 300)
        # 后两个参数确定了它的尺寸,效果等同于self.resize(300, 200)
        self.setGeometry(300, 300, 300, 220)

        self.setWindowTitle('Icon')

        self.setWindowIcon(QIcon('/home/linux/1.jpg'))   #设置窗口图标

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())
