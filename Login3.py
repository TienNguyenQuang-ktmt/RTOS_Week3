# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login3.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import source_login
import Main3
import Error3
import sqlite3

data = sqlite3.connect("taikhoan.db")

da = data.cursor()
da.execute('''create table if not exists TAIKHOAN(Name char[10],Pass char[10])''')
data.commit()

class Ui_LoginWindow(object):
    stateLogin =False
    def LoginSuccess(self):#open MainWindow
        #check account in database
        userName = self.edtName.toPlainText()
        password = self.edtPass.toPlainText()
        getName = da.execute("select * from TAIKHOAN")
        for i in getName:
            if str(i[0])==userName:
                if str(i[1])==password:
                    #check account in database TAIKHOAN
                    #set value for login: open function SucessLogin
                    self.stateLogin =True
                    self.label_3.setText("OK")
        if self.stateLogin:
            self.window = QtWidgets.QMainWindow()
            self.ui = Main3.Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.LoginUnsucess()
        #right account
    def LoginUnsucess(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Error3.Ui_ErrorWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(678, 495)
        LoginWindow.setStyleSheet("background-image: url(:/background1/backgroundcolorful.jpg);\n"
"")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.edtName = QtWidgets.QTextEdit(self.centralwidget)
        self.edtName.setGeometry(QtCore.QRect(270, 250, 211, 31))
        self.edtName.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.edtName.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.edtName.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(0, 255, 255, 255))")
        self.edtName.setObjectName("edtName")
        self.edtPass = QtWidgets.QTextEdit(self.centralwidget)
        self.edtPass.setGeometry(QtCore.QRect(270, 300, 211, 31))
        self.edtPass.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(0, 255, 255, 255))")
        self.edtPass.setObjectName("edtPass")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 260, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Tekton Pro")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.25 rgba(32, 34, 84, 255), stop:1 rgba(3, 4, 38, 255))    ;\n"
"    color: rgb(255, 85, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(186, 302, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Tekton Pro")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.25 rgba(32, 34, 84, 255), stop:1 rgba(3, 4, 38, 255))    ;\n"
"    color: rgb(255, 85, 0);")
        self.label_2.setObjectName("label_2")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(270, 350, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(10)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(67, 67, 67, 255));\n"
"color: rgb(255, 255, 127);")
        self.btnLogin.setObjectName("btnLogin")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 50, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.label_3.setObjectName("label_3")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        self.btnLogin.clicked.connect(self.LoginSuccess)
        self.btnLogin.clicked.connect(LoginWindow.close)


    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.edtName.setPlaceholderText(_translate("LoginWindow", "ten dang nhap"))
        self.edtPass.setPlaceholderText(_translate("LoginWindow", "mat khau"))
        self.label.setText(_translate("LoginWindow", "User"))
        self.label_2.setText(_translate("LoginWindow", "Password"))
        self.btnLogin.setText(_translate("LoginWindow", "Login"))
        self.label_3.setText(_translate("LoginWindow", "BAI THUC HANH SO 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
