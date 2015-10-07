# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Feb  3 21:34:24 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(871, 611)

        self.centralwidget  = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 0, 871, 611))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        

        self.groupBox = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox.setGeometry(QtCore.QRect(0, 410, 401, 181))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        
        self.commandLinkButton_5 = QtGui.QCommandLinkButton(self.groupBox)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(20, 90, 211, 41))
        self.commandLinkButton_5.setObjectName(_fromUtf8("commandLinkButton_5"))
        
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 371, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 90, 151, 41))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 30, 401, 231))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 121, 61))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        self.lcdNumber = QtGui.QLCDNumber(self.groupBox_2)
        self.lcdNumber.setGeometry(QtCore.QRect(170, 30, 211, 31))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.lcdNumber.setNumDigits(14)
        self.lcdNumber.setSegmentStyle(2)
        self.lcdNumber.display("123456789")

        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 70, 121, 61))
        self.label.setObjectName(_fromUtf8("label"))
        
        self.lcdNumber_2 = QtGui.QLCDNumber(self.groupBox_2)
        self.lcdNumber_2.setGeometry(QtCore.QRect(170, 90, 211, 31))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(410, 30, 461, 561))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))

        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(50, 364, 371, 51))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 474, 351, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.pushButton = QtGui.QPushButton(self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(60, 420, 351, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        
        self.progressBar = QtGui.QProgressBar(self.groupBox_3)
        self.progressBar.setGeometry(QtCore.QRect(20, 310, 371, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))

        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(30, 270, 361, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.commandLinkButton_5.setText(_translate("MainWindow", "SEND", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Balance:</span></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Unconfirmed</span></p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">1aw3s4dNnk234jnd2d34d2tmPwkmQrR5</span></p></body></html>", None))
        self.pushButton_3.setText(_translate("MainWindow", "Log out", None))
        self.pushButton.setText(_translate("MainWindow", "New Address", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Connecting to server..............................</span></p></body></html>", None))







def main():
    
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QMainWindow()
    w.setWindowTitle('Simple')
    insi = Ui_MainWindow()
    insi.setupUi(w)
    insi.retranslateUi(w)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()  














