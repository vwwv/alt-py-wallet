# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pin.ui'
#
# Created: Wed Feb  4 06:20:09 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(558, 472)
        self.groupBox_10 = QtGui.QGroupBox(Dialog)
        self.groupBox_10.setGeometry(QtCore.QRect(-10, 0, 571, 421))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_10)
        self.groupBox_7.setGeometry(QtCore.QRect(220, 290, 151, 101))
        self.groupBox_7.setTitle(_fromUtf8(""))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 20, 91, 61))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_10)
        self.groupBox_4.setGeometry(QtCore.QRect(220, 170, 151, 101))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 20, 91, 61))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_10)
        self.groupBox_8.setGeometry(QtCore.QRect(40, 290, 151, 101))
        self.groupBox_8.setTitle(_fromUtf8(""))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_8)
        self.pushButton_8.setGeometry(QtCore.QRect(30, 20, 91, 61))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox_10)
        self.groupBox_9.setGeometry(QtCore.QRect(400, 290, 151, 101))
        self.groupBox_9.setTitle(_fromUtf8(""))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_9)
        self.pushButton_9.setGeometry(QtCore.QRect(30, 20, 91, 61))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_10)
        self.groupBox_2.setGeometry(QtCore.QRect(220, 50, 151, 101))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 20, 91, 61))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.groupBox = QtGui.QGroupBox(self.groupBox_10)
        self.groupBox.setGeometry(QtCore.QRect(40, 50, 151, 101))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 91, 61))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_10)
        self.groupBox_6.setGeometry(QtCore.QRect(400, 170, 151, 101))
        self.groupBox_6.setTitle(_fromUtf8(""))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 20, 91, 61))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_10)
        self.groupBox_3.setGeometry(QtCore.QRect(400, 50, 151, 101))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 20, 91, 61))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_10)
        self.groupBox_5.setGeometry(QtCore.QRect(40, 170, 151, 101))
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 20, 91, 61))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox_10.setTitle(_translate("Dialog", "Enter the secret Pin the layout as shown on the device:", None))
        self.pushButton_7.setText(_translate("Dialog", "?", None))
        self.pushButton_4.setText(_translate("Dialog", "?", None))
        self.pushButton_8.setText(_translate("Dialog", "?", None))
        self.pushButton_9.setText(_translate("Dialog", "?", None))
        self.pushButton_2.setText(_translate("Dialog", "?", None))
        self.pushButton.setText(_translate("Dialog", "?", None))
        self.pushButton_6.setText(_translate("Dialog", "?", None))
        self.pushButton_3.setText(_translate("Dialog", "?", None))
        self.pushButton_5.setText(_translate("Dialog", "?", None))

