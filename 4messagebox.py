#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

class Myform(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('message box')
        self.show()
    # closeEvent的重新实现
    def closeEvent(self, e):
        # 参数从左到右: self, 提示窗口标题, 提示信息, 两个按钮, 默认选中
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())



