#! /usr/bin/python
# -*- coding: UTF-8 -*-
 
import sys
from PyQt4 import QtGui
from converter import Ui_MainWindow
 
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
 
    def fromValueChanged(self, v):
        self.toValue.setText(str(v*1.609344))
 
app = QtGui.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
