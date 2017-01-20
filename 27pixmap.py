#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt


class Myform(QWidget):

    def __init__(self):

        super(Myform, self).__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)
        self.pixmap = QPixmap('1.jpg')

        lbl = QLabel(self)
        lbl.setPixmap(self.pixmap)    # 设置标签内容图片

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 300)
        self.resize(1000, 1000)
        self.setWindowTitle('pixmap')
        self.show()

    def paintEvent(self, QPaintEvent):

        painter = QPainter(self)
        painter.translate(600, 100)     # 将(600, 100)设为新图的原点
        # 后四位参素是从图片的(80, 100)位置截取横300,纵100像素的图片,并根据前四位参数对像素图的大小位置设置
        painter.rotate(150)    # 顺时针旋转150度
        painter.scale(2, 2)    # 横纵坐标放大两倍(原点位置不变)
        painter.drawPixmap(0, 0, 300, 200, self.pixmap, 80, 100, 300, 100)
        painter.translate(100, 100)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())