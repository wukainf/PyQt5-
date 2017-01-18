#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QAction
from PyQt5.QtGui import QIcon


class Myform(QMainWindow):

    def __init__(self):

        super(Myform, self).__init__()
        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()


        openFile = QAction(QIcon('1.jpg'), 'Open', self)
        openFile.setStatusTip('Open new File')
        openFile.setShortcut('Ctrl+O')
        openFile.triggered.connect(self.showDialog)

        toolbar = self.addToolBar('Openfile')
        toolbar.addAction(openFile)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('filedialog')
        self.show()

    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home/linux')   #FilePicker

        if fname[0]:
            with open(fname[0], 'r') as f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Myform()
    sys.exit(app.exec_())

