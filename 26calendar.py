#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel
from PyQt5.QtCore import QDate


class Myform(QWidget):

    def __init__(self):

        super(Myform, self).__init__()

        self.initUI()

    def initUI(self):

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)    # 让日历网格状显示
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)  # 触发事件并传递参数QDate(选中日期)

        self.lbl = QLabel(self)

        date = cal.selectedDate()   # 显示默认选中的日期
        self.lbl.setText(date.toString())

        self.lbl.move(130, 260)

        self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle("cadenlar")
        self.show()

    def showDate(self, date):

        self.lbl.setText(date.toString())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())