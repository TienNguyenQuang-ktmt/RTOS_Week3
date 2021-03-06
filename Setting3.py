from PyQt5 import QtCore, QtGui, QtWidgets
import Main3
import sqlite3
#create database for value of temperature and humidity setting
data = sqlite3.connect("setting.db")
da = data.cursor()
da.execute('''create table if not exists SETTING(id int,temperature int,humidity int)''')
#da.execute("INSERT INTO SETTING VALUES(1,27,30)")
data.commit()
class Ui_SettingWindow(object):
    def OpenMainWindow(self):
        #Save vlaue in database
        t = self.sliderTemp.value()
        h = self.sliderHumid.value()
        da.execute('DELETE FROM SETTING;',)
        valueTable=(
            (1,t,h)
        )
        da.execute("INSERT INTO SETTING VALUES(?,?,?)",valueTable)
        data.commit()

        self.window = QtWidgets.QMainWindow()
        self.ui = Main3.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, SettingWindow):
        SettingWindow.setObjectName("SettingWindow")
        SettingWindow.resize(311, 355)
        SettingWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.840909 rgba(170, 255, 127, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(SettingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 82, 28))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(170, 255, 127, 255));")
        self.label_2.setObjectName("label_2")
        self.sliderTemp = QtWidgets.QSlider(self.centralwidget)
        self.sliderTemp.setGeometry(QtCore.QRect(49, 110, 211, 22))
        self.sliderTemp.setOrientation(QtCore.Qt.Horizontal)
        self.sliderTemp.setObjectName("sliderTemp")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 140, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tvValueTemp = QtWidgets.QLabel(self.centralwidget)
        self.tvValueTemp.setGeometry(QtCore.QRect(220, 140, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tvValueTemp.setFont(font)
        self.tvValueTemp.setObjectName("tvValueTemp")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 230, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 230, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tvValueHumid = QtWidgets.QLabel(self.centralwidget)
        self.tvValueHumid.setGeometry(QtCore.QRect(220, 230, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tvValueHumid.setFont(font)
        self.tvValueHumid.setObjectName("tvValueHumid")
        self.sliderHumid = QtWidgets.QSlider(self.centralwidget)
        self.sliderHumid.setGeometry(QtCore.QRect(49, 200, 211, 22))
        self.sliderHumid.setOrientation(QtCore.Qt.Horizontal)
        self.sliderHumid.setObjectName("sliderHumid")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(170, 255, 127, 255));")
        self.label_9.setObjectName("label_9")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(120, 290, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setBold(True)
        font.setWeight(75)
        self.btnSave.setFont(font)
        self.btnSave.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.495 rgba(255, 255, 255, 255), stop:0.505 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.btnSave.setObjectName("btnSave")
        SettingWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(SettingWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingWindow)
        #read database when Ui open(only one)
        getId = da.execute("SELECT * FROM SETTING")
        for i in getId:
            self.sliderTemp.setValue(i[1])
            self.sliderHumid.setValue(i[2])
            self.tvValueHumid.setText(str(self.sliderHumid.value()))
            self.tvValueTemp.setText(str(self.sliderTemp.value()))
        ############3
        #event button
        self.btnSave.clicked.connect(self.OpenMainWindow)
        self.btnSave.clicked.connect(SettingWindow.close)
        
        #event slider
        self.sliderTemp.valueChanged.connect(self.SliderTempChanged)
        self.sliderHumid.valueChanged.connect(self.SliderHumidChanged)

    def SliderTempChanged(self):
        valueTemp = self.sliderTemp.value()
        self.tvValueTemp.setText(str(valueTemp))

    def SliderHumidChanged(self):
        valuaHumid = self.sliderHumid.value()
        self.tvValueHumid.setText(str(valuaHumid))
    def retranslateUi(self, SettingWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingWindow.setWindowTitle(_translate("SettingWindow", "Settings"))
        self.label.setText(_translate("SettingWindow", "Settings"))
        self.label_2.setText(_translate("SettingWindow", "<html><head/><body><p>limit temperature</p></body></html>"))
        self.label_3.setText(_translate("SettingWindow", "0"))
        self.label_4.setText(_translate("SettingWindow", "<html><head/><body><p><span style=\" vertical-align:super;\">0</span>C</p></body></html>"))
        self.tvValueTemp.setText(_translate("SettingWindow", "<html><head/><body><p align=\"right\">37</p></body></html>"))
        self.label_6.setText(_translate("SettingWindow", "<html><head/><body><p>%</p></body></html>"))
        self.label_7.setText(_translate("SettingWindow", "0"))
        self.tvValueHumid.setText(_translate("SettingWindow", "<html><head/><body><p align=\"right\">50</p></body></html>"))
        self.label_9.setText(_translate("SettingWindow", "<html><head/><body><p>limit humidity</p></body></html>"))
        self.btnSave.setText(_translate("SettingWindow", "Save"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingWindow = QtWidgets.QMainWindow()
    ui = Ui_SettingWindow()
    ui.setupUi(SettingWindow)
    SettingWindow.show()
    sys.exit(app.exec_())
