# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Error3.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Login3

class Ui_ErrorWindow(object):
    def LoginWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Login3.Ui_LoginWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, ErrorWindow):
        ErrorWindow.setObjectName("ErrorWindow")
        ErrorWindow.resize(361, 160)
        ErrorWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.559, y1:0.431955, x2:0.559, y2:0.767045, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(ErrorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnYes = QtWidgets.QPushButton(self.centralwidget)
        self.btnYes.setGeometry(QtCore.QRect(80, 110, 75, 23))
        self.btnYes.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.989, y1:0.982955, x2:1, y2:1, stop:0 rgba(255, 170, 127, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btnYes.setObjectName("btnYes")
        self.btnNo = QtWidgets.QPushButton(self.centralwidget)
        self.btnNo.setGeometry(QtCore.QRect(200, 110, 75, 23))
        self.btnNo.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.989, y1:0.982955, x2:1, y2:1, stop:0 rgba(255, 170, 127, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btnNo.setObjectName("btnNo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        ErrorWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ErrorWindow)
        QtCore.QMetaObject.connectSlotsByName(ErrorWindow)
        #event button
        self.btnYes.clicked.connect(self.LoginWindow)
        self.btnYes.clicked.connect(ErrorWindow.close)
        self.btnNo.clicked.connect(ErrorWindow.close)

    def retranslateUi(self, ErrorWindow):
        _translate = QtCore.QCoreApplication.translate
        ErrorWindow.setWindowTitle(_translate("ErrorWindow", "Error"))
        self.btnYes.setText(_translate("ErrorWindow", "Yes"))
        self.btnNo.setText(_translate("ErrorWindow", "No"))
        self.label.setText(_translate("ErrorWindow", "<html><head/><body><p align=\"center\">Sai Mat Khau!</p><p align=\"center\">Ban co muon dang nhap lai</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ErrorWindow = QtWidgets.QMainWindow()
    ui = Ui_ErrorWindow()
    ui.setupUi(ErrorWindow)
    ErrorWindow.show()
    sys.exit(app.exec_())
