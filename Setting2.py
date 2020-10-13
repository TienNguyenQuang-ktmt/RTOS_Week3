# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Seting.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import Main2
class Ui_SetWindow(object):
    def openMainWindow(self):
        self.windowMain =QtWidgets.QMainWindow()
        self.ui =Main2.Ui_MainWindow()
        self.ui.setup(self.windowMain)
        self.windowMain.show()

    def setupUi(self, SetWindow):
        SetWindow.setObjectName("SetWindow")
        SetWindow.resize(383, 224)
        self.centralwidget = QtWidgets.QWidget(SetWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnBackMain = QtWidgets.QPushButton(self.centralwidget)
        self.btnBackMain.setGeometry(QtCore.QRect(200, 140, 75, 23))
        self.btnBackMain.setObjectName("btnBackMain")
        SetWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SetWindow)
        QtCore.QMetaObject.connectSlotsByName(SetWindow)
        #############
        self.btnBackMain.clicked.connect(self.openMainWindow)
        self.btnBackMain.clicked.connect(SetWindow.close)

    def retranslateUi(self, SetWindow):
        _translate = QtCore.QCoreApplication.translate
        SetWindow.setWindowTitle(_translate("SetWindow", "SettingsWindow"))
        self.btnBackMain.setText(_translate("SetWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SetWindow = QtWidgets.QMainWindow()
    ui = Ui_SetWindow()
    ui.setupUi(SetWindow)
    SetWindow.show()
    sys.exit(app.exec_())
