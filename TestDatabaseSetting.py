import sqlite3
#create database for value of temperature and humidity setting
data = sqlite3.connect("setting.db")
da = data.cursor()
da.execute('''create table if not exists SETTING(id int,temperature int,humidity int)''')
#da.execute("INSERT INTO SETTING VALUES(1,27,30)")
data.commit()
dataa = da.execute("SELECT * FROM SETTING") #mssv,hoten,rtos thay the bang * de lay het
for i in dataa:
    print("------------*------------")
    print("Id:   " + str(i[0]))
    print("TEMP:   " + str(i[1]))
    print("HUMID:   " + str(i[2]))
data.close()