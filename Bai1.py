from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

data = sqlite3.connect("taikhoan.db")

da = data.cursor()
da.execute('''create table if not exists TAIKHOAN(Name char[10],Pass char[10])''')
#da.execute("INSERT INTO TAIKHOAN VALUES('tien','1999')")
#da.execute("INSERT INTO TAIKHOAN VALUES('tien123','123456')")

data.commit()
count=0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 324)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 60, 47, 13))
        self.label.setObjectName("label")
        self.edtUser = QtWidgets.QTextEdit(self.centralwidget)
        self.edtUser.setGeometry(QtCore.QRect(140, 50, 181, 31))
        self.edtUser.setObjectName("edtUser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 0, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 51, 20))
        self.label_3.setObjectName("label_3")
        self.edtPass = QtWidgets.QTextEdit(self.centralwidget)
        self.edtPass.setGeometry(QtCore.QRect(140, 100, 181, 31))
        self.edtPass.setObjectName("edtPass")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(10, 180, 75, 23))
        self.btnAdd.setObjectName("btnAdd")
        self.btnDel = QtWidgets.QPushButton(self.centralwidget)
        self.btnDel.setGeometry(QtCore.QRect(100, 180, 75, 23))
        self.btnDel.setObjectName("btnDel")
        self.btnEdit = QtWidgets.QPushButton(self.centralwidget)
        self.btnEdit.setGeometry(QtCore.QRect(190, 180, 75, 23))
        self.btnEdit.setObjectName("btnEdit")
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(280, 180, 75, 23))
        self.btnSearch.setObjectName("btnSearch")
        self.btnShow = QtWidgets.QPushButton(self.centralwidget)
        self.btnShow.setGeometry(QtCore.QRect(370, 180, 75, 23))
        self.btnShow.setObjectName("btnShow")
        self.tvName = QtWidgets.QLabel(self.centralwidget)
        self.tvName.setGeometry(QtCore.QRect(40, 230, 171, 71))
        self.tvName.setText("")
        self.tvName.setObjectName("tvName")
        self.tvPass = QtWidgets.QLabel(self.centralwidget)
        self.tvPass.setGeometry(QtCore.QRect(240, 230, 171, 71))
        self.tvPass.setText("")
        self.tvPass.setObjectName("tvPass")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ##xu ly nut nhan
        self.btnSearch.clicked.connect(self.FunctionSearch)
        self.btnShow.clicked.connect(self.FunctionShow)
        self.btnAdd.clicked.connect(self.FunctionAdd)
        self.btnDel.clicked.connect(self.FunctionDel)
        self.btnEdit.clicked.connect(self.FunctionEdit)

    def FunctionEdit(self):
        if self.tvPass.text()=="nhap moi":
            self.count =2
        else: 
            self.tvPass.setText("nhap moi")
            self.count= 1
        nameUser=" "
        passUser=" "
        if self.count ==1:
            searchName = self.edtUser.toPlainText()
            getName = da.execute("select * from TAIKHOAN")
            error=True
            for i in getName:
                if str(i[0])==searchName:
                    if str(i[1])==self.edtPass.toPlainText():
                        error = False
                        nameUser = searchName
            if error:
                self.tvName.setText("Not Found")
            else:
            #userDel(
            #    (nameUser,passUser)
            #)
                da.execute("delete from TAIKHOAN where Name=?", (nameUser,))
                data.commit()
                self.tvName.setText("Dang chinh sua")
        elif self.count ==2:
            nameUser = self.edtUser.toPlainText()
            passUser = self.edtPass.toPlainText()
            user= (
                (nameUser,passUser)
            )
            da.execute("INSERT INTO TAIKHOAN VALUES(?,?)",user)
            data.commit()
            self.tvName.setText("Da them tai khoan")
            self.tvPass.setText(nameUser)
            self.count=0
        

    def FunctionDel(self):
        nameUser=" "
        passUser=" "
        searchName = self.edtUser.toPlainText()
        getName = da.execute("select * from TAIKHOAN")
        error=True
        for i in getName:
            if str(i[0])==searchName:
                if str(i[1])==self.edtPass.toPlainText():
                    error = False
                    nameUser = searchName
        if error:
            self.tvName.setText("Not Found")
            self.tvPass.setText(" ")
        else:
            #userDel(
            #    (nameUser,passUser)
            #)
            da.execute("delete from TAIKHOAN where Name=?", (nameUser,))
            data.commit()
            self.tvName.setText("Da xoa thanh cong tai khoan")
            self.tvPass.setText(nameUser)

    def FunctionAdd(self):
        nameUser=" "
        passUser=" "
        searchName = self.edtUser.toPlainText()
        getName = da.execute("select * from TAIKHOAN")
        error=False
        for i in getName:
            if str(i[0])==searchName:
                error = True
        if error:
            self.tvName.setText("Ten tai khoan ton tai")
            self.tvPass.setText(" ")
        else:
            nameUser= searchName
            passUser= self.edtPass.toPlainText()
            user= (
                (nameUser,passUser)
            )
            da.execute("INSERT INTO TAIKHOAN VALUES(?,?)",user)
            data.commit()

    def FunctionSearch(self):
        nameUser=" "
        passUser=" "
        searchName = self.edtUser.toPlainText()
        getName = da.execute("select * from TAIKHOAN")
        error=True
        for i in getName:
            if str(i[0])==searchName:
                error = False
                nameUser = str(i[0])
                passUser = str(i[1])
                self.tvName.setText(nameUser)
                self.tvPass.setText(passUser)
        if error:
            self.tvName.setText("Not Found")
            self.tvPass.setText(" ")
    def FunctionShow(self):
        nameUser=""
        passUser=""
        searchName = self.edtUser.toPlainText()
        getName = da.execute("select * from TAIKHOAN")
        for i in getName:
            nameUser = nameUser+ str(i[0])+"\n"
            passUser = passUser+ str(i[1])+"\n"
        self.tvName.setText(nameUser)
        self.tvPass.setText(passUser)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "User"))
        self.label_2.setText(_translate("MainWindow", "User Database"))
        self.label_3.setText(_translate("MainWindow", "password"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnDel.setText(_translate("MainWindow", "Delete"))
        self.btnEdit.setText(_translate("MainWindow", "Edit"))
        self.btnSearch.setText(_translate("MainWindow", "Search"))
        self.btnShow.setText(_translate("MainWindow", "Show"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
