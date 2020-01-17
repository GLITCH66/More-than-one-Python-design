#! /usr/bin/python
# -*- coding: UTF-8 -*-
import sys
from PyQt4 import QtGui
 
app = QtGui.QApplication(sys.argv)
n, ok = QtGui.QInputDialog.getText(None, u"مرحبا يا عالم!", u"فضلا اكتب اسمك:")
if ok and n:
    QtGui.QMessageBox.information(None, u"أهلا بك في Qt", u"مرحبا بك يا "+n+u"!")
else:
    QtGui.QMessageBox.information(None, u"أهلا بك في Qt", u"أنت لم تكتب اسما")
