# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main3.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import source_main
import Login3
import Setting3
import sqlite3
#create database for value of temperature and humidity setting
data = sqlite3.connect("setting.db")
da = data.cursor()
da.execute('''create table if not exists SETTING(id int,temperature int,humidity int)''')
data.commit()

class Ui_MainWindow(object):
    stateFan=False
    stateLamp=False
    def LogoutMainWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Login3.Ui_LoginWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def OpenSettingWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Setting3.Ui_SettingWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(545, 388)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.989, y1:0.982955, x2:1, y2:1, stop:0 rgba(255, 170, 127, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(160, 60, 31, 31))
        self.frame.setStyleSheet("background-image: url(:/bg_image/icontemperature.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(160, 100, 31, 31))
        self.frame_2.setStyleSheet("background-image: url(:/bg_image/iconhumidity.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tvTemp = QtWidgets.QLabel(self.centralwidget)
        self.tvTemp.setGeometry(QtCore.QRect(240, 60, 150, 31))
        self.tvTemp.setObjectName("tvTemp")
        self.tvHumid = QtWidgets.QLabel(self.centralwidget)
        self.tvHumid.setGeometry(QtCore.QRect(240, 100, 150, 31))
        self.tvHumid.setObjectName("tvHumid")
        self.btnSetting = QtWidgets.QPushButton(self.centralwidget)
        self.btnSetting.setGeometry(QtCore.QRect(460, 20, 35, 35))
        self.btnSetting.setStyleSheet("background-image:url(:/bg_image/setting30px.png)")
        self.btnSetting.setText("")
        self.btnSetting.setObjectName("btnSetting")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 150, 511, 221))
        self.frame_3.setStyleSheet("background: qlineargradient(spread:pad, x1:0.829545, y1:0.739, x2:1, y2:1, stop:0 rgba(255, 123, 97, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.groupBox = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 150, 120, 41))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioOn = QtWidgets.QRadioButton(self.groupBox)
        self.radioOn.setGeometry(QtCore.QRect(10, 10, 41, 17))
        self.radioOn.setObjectName("radioOn")
        self.radioOff = QtWidgets.QRadioButton(self.groupBox)
        self.radioOff.setGeometry(QtCore.QRect(70, 10, 41, 17))
        self.radioOff.setObjectName("radioOff")
        self.radioOff.setChecked(True)
        self.btnFan = QtWidgets.QPushButton(self.frame_3)
        self.btnFan.setGeometry(QtCore.QRect(210, 160, 75, 23))
        self.btnFan.setObjectName("btnFan")
        self.sliderMotor = QtWidgets.QSlider(self.frame_3)
        self.sliderMotor.setGeometry(QtCore.QRect(370, 160, 101, 22))
        self.sliderMotor.setOrientation(QtCore.Qt.Horizontal)
        self.sliderMotor.setObjectName("sliderMotor")
        self.frameLamp = QtWidgets.QFrame(self.frame_3)
        self.frameLamp.setGeometry(QtCore.QRect(20, 20, 111, 101))
        self.frameLamp.setStyleSheet("\n"
"background-image: url(:/bg_image/lampbulboff100px.png);")
        self.frameLamp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLamp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLamp.setObjectName("frameLamp")
        self.frameFan = QtWidgets.QFrame(self.frame_3)
        self.frameFan.setGeometry(QtCore.QRect(190, 20, 111, 101))
        self.frameFan.setStyleSheet("background-image: url(:/bg_image/electricfanoff100px.png);")
        self.frameFan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameFan.setObjectName("frameFan")
        self.frameMotor = QtWidgets.QFrame(self.frame_3)
        self.frameMotor.setGeometry(QtCore.QRect(370, 20, 111, 101))
        self.frameMotor.setStyleSheet("background-image: url(:/bg_image/pumpon100px.png);")
        self.frameMotor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMotor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMotor.setObjectName("frameMotor")
        self.btnLogout = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogout.setGeometry(QtCore.QRect(500, 20, 35, 35))
        self.btnLogout.setStyleSheet("background-image: url(:/bg_image/power30px.png);")
        self.btnLogout.setText("")
        self.btnLogout.setObjectName("btnLogout")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        getId = da.execute("SELECT * FROM SETTING")
        for i in getId:
            self.tvTemp.setText(str(i[1])+" C degree")
            self.tvHumid.setText(str(i[2])+" %")
        ############3
        #event button system
        self.btnLogout.clicked.connect(self.LogoutMainWindow)
        self.btnLogout.clicked.connect(MainWindow.close)
        self.btnSetting.clicked.connect(self.OpenSettingWindow)
        self.btnSetting.clicked.connect(MainWindow.close)
        #event button function
        self.btnFan.clicked.connect(self.FunctionFan)
        self.radioOn.toggled.connect(self.FunctionLamp)
        self.radioOff.toggled.connect(self.FunctionLamp)
        self.sliderMotor.valueChanged.connect(self.FunctionMotor)
    
    def FunctionMotor(self):
        valueSlider =self.sliderMotor.value()/100
        stringValue = "background-color: qlineargradient(spread:pad, x1:"+str(valueSlider)+", y1:0.739, x2:1, y2:1, stop:0 rgba(255, 123, 97, 255), stop:1 rgba(255, 255, 255, 255));background-image: url(:/bg_image/pumpon100px.png);"
        self.frameMotor.setStyleSheet(stringValue)

    def FunctionLamp(self):
        if self.radioOff.isChecked()==True:
            self.frameLamp.setStyleSheet("background-image: url(:/bg_image/lampbulboff100px.png);")
        elif self.radioOn.isChecked()==True:
            self.frameLamp.setStyleSheet("background-image: url(:/bg_image/lampbulbon100px.png);")
    def FunctionFan(self):
        self.stateFan = not self.stateFan
        if self.stateFan:
            self.frameFan.setStyleSheet("background-image: url(:/bg_image/electricfanon100px.png);")
        else:
            self.frameFan.setStyleSheet("background-image: url(:/bg_image/electricfanoff100px.png);")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Màn Hình Chính"))
        self.tvTemp.setText(_translate("MainWindow", "nhiet"))
        self.tvHumid.setText(_translate("MainWindow", "do am"))
        self.radioOn.setText(_translate("MainWindow", "ON"))
        self.radioOff.setText(_translate("MainWindow", "OFF"))
        self.btnFan.setText(_translate("MainWindow", "ON/OFF"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
