#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt

class Myform(QWidget):

    def __init__(self):

        super(QWidget, self).__init__()
        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)      # 创建一个数字显示器
        sld = QSlider(Qt.Horizontal, self)    # 创建一个拖动条

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)

        # signal & slot:当拖动条的值改变触发事件(值显示到数字板上)
        #              信号(事件源)   槽(事件对象)     事件目标
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('signalslot')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())