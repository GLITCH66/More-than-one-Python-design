#! /usr/bin/python
# -*- coding: UTF-8 -*-
import sys
from PyQt4 import QtGui
 
app = QtGui.QApplication(sys.argv)
 
reply=QtGui.QMessageBox.Yes
while(reply == QtGui.QMessageBox.Yes):
    w, ok = QtGui.QInputDialog.getDouble(None, u"مساحة المستطيل!", u"فضلا ادخل طول المستطيل:")
    if ok:
      h, ok = QtGui.QInputDialog.getDouble(None, u"مساحة المستطيل!", u"فضلا ادخل عرض المستطيل:")
 
    if ok:
        a=w*h
        QtGui.QMessageBox.information(None, u"مساحة المستطيل",
            u"مساحة المستطيل الذي أدخلته تساوي "+str(a))
 
    reply=QtGui.QMessageBox.question(None, u"مساحة المستطيل",
            u"هل تريد المحاولة من جديد؟",
            QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
