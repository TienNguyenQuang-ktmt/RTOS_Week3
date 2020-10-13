from PyQt5 import QtCore, QtGui, QtWidgets
#from Login2 import Ui_LoginWindow
import Login2
import Setting2
class Ui_MainWindow(object):

    def openLoginWindow(self):
        self.window2 =QtWidgets.QMainWindow()
        self.ui =Login2.Ui_LoginWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()
        
    def openSetting(self):
        self.window =QtWidgets.QMainWindow()
        self.ui =Setting2.Ui_SetWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setup(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 251)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnSetting = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetting.setGeometry(QtCore.QRect(150, 120, 75, 23))
        self.btnSetting.setObjectName("btnSetting")
        self.btnOut = QtWidgets.QPushButton(self.centralwidget)
        self.btnOut.setGeometry(QtCore.QRect(150, 170, 75, 23))
        self.btnOut.setObjectName("btnOut")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #xu ly nut nhan
        self.btnOut.clicked.connect(self.openLoginWindow)
        self.btnOut.clicked.connect(MainWindow.close)
        self.btnSetting.clicked.connect(self.openSetting)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnSetting.setText(_translate("MainWindow", "Settings"))
        self.btnOut.setText(_translate("MainWindow", "Log out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
