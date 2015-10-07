# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Feb  4 19:16:00 2015
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
        Dialog.resize(878, 628)
        self.centralwidget = QtGui.QWidget(Dialog)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 881, 631))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(-10, 20, 401, 231))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 121, 61))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lcdNumber = QtGui.QLCDNumber(self.groupBox_2)
        self.lcdNumber.setGeometry(QtCore.QRect(170, 30, 211, 31))
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setNumDigits(12)
        self.lcdNumber.setDigitCount(12)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber.display(234)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 70, 121, 61))
        self.label.setObjectName(_fromUtf8("label"))
        self.lcdNumber_2 = QtGui.QLCDNumber(self.groupBox_2)
        self.lcdNumber_2.setGeometry(QtCore.QRect(170, 90, 211, 31))
        self.lcdNumber_2.setSmallDecimalPoint(True)
        self.lcdNumber_2.setNumDigits(12)
        self.lcdNumber_2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_2.setProperty("value", 0.300187)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(-10, 400, 401, 181))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.commandLinkButton_5 = QtGui.QCommandLinkButton(self.groupBox)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(20, 90, 211, 41))
        self.commandLinkButton_5.setObjectName(_fromUtf8("commandLinkButton_5"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 371, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 90, 151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(10, 340, 371, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 310, 361, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(420, 20, 461, 561))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(50, 310, 371, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(True)
        self.label_3.setFrameShadow(QtGui.QFrame.Plain)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 470, 351, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton = QtGui.QPushButton(self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(60, 420, 351, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 370, 351, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        
        self.frame = QtGui.QLabel(self.groupBox_4)
        self.frame.setGeometry(QtCore.QRect(90, 20, 271, 251))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(100, 20, 481, 41))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tableView = QtGui.QTableView(self.tab_2)
        self.tableView.setGeometry(QtCore.QRect(-10, 70, 891, 541))
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(100)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "MainWindow", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Balance:</span></p></body></html>", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Unconfirmed</span></p></body></html>", None))
        self.commandLinkButton_5.setText(_translate("Dialog", "SEND", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Connecting to server..............................</span></p></body></html>", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">1aw3s4dNnk234jnd2d34d2tmPwkmQrR5</span></p></body></html>", None))
        self.pushButton_3.setText(_translate("Dialog", "Log out", None))
        self.pushButton.setText(_translate("Dialog", "Copy to clipboard", None))
        self.pushButton_2.setText(_translate("Dialog", "New Address", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Main Menu", None))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">Transaction And Balance History:</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Transaction History", None))

