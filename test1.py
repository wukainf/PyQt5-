#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)   #创建QApplication对象

    w = QWidget()     #创建QWidget对象
    w.resize( 250, 150 )        #创建窗体大小
    w.move( 100, 300 )       #设置在屏幕上的显示位置
    w.setWindowTitle( 'hello world agian' )      #设置窗口标题
    w.show()           #窗口显示

    sys.exit( app.exec_() )
