#!/usr/bin/python

import mysql.connector
from mysql.connector import errorcode
from datetime import datetime



KEYWORD = dict()
KEYWORD = {'bng':4}
KEYWORD['ang'] = int(3)
print(KEYWORD)

class DatabaseUtility:
    def __init__(self, database, tableName):
        self.db = database

        self.tableName = tableName
        self.cnx = mysql.connector.connect(user='root', password='Ms5276262*', host='127.0.0.1')
        # cnx = connection; extablishing conncection
        self.cursor = self.cnx.cursor()

        self.connectToDatabase()
        self.createTable()

    def connectToDatabase(self):
        try:
            self.cnx.database = self.db
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.createDatabase()
                self.cnx.database = self.db
            else:
                print(err.msg)

    def createDatabase(self):
        try:
            self.runCommand("CREATE DATABASE %s DEFAULT CHARACTER SET 'utf8';" % self.db)
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))

    # " `message` char(50) NOT NULL,"
    def createTable(self):
        #여기선 추가적으로 추가/제거가 힘들고 mysql터미널에서 직접 해 주어야 함!



        cmd = (" CREATE TABLE IF NOT EXISTS " + self.tableName + " ("
                                                                 " `ID` int(5) NOT NULL AUTO_INCREMENT,"
                                                                 " `date` date NOT NULL,"
                                                                 " `time` time NOT NULL,"
                                                                 " `message` char(50) NOT NULL,"
                                                                 " PRIMARY KEY (`ID`)"
                                                                 ") ENGINE=InnoDB;")
        self.runCommand(cmd)

    def getTable(self):
        self.createTable()
        return self.runCommand("SELECT * FROM %s;" % self.tableName)

    def getColumns(self):
        return self.runCommand("SHOW COLUMNS FROM %s;" % self.tableName)

    def runCommand(self, cmd):
        print("RUNNING COMMAND: " + cmd)
        try:
            self.cursor.execute(cmd)
        except mysql.connector.Error as err:
            print('ERROR MESSAGE: ' + str(err.msg))
            print('WITH ' + cmd)
        try:
            msg = self.cursor.fetchall()
        except:
            msg = self.cursor.fetchone()
        return msg

    def addEntryToTable(self):
        date1 = datetime.now().strftime("%y-%m-%d")
        time = datetime.now().strftime("%H:%M")

        cmd = " INSERT INTO " + self.tableName + " (`date`, `time`)"
        cmd += " VALUES ('%s', '%s');" % (date1, time)
        "where"

        #딕트쌍으로 과목-인상시킬 포인트를 짜고, 스트링테크닉으로 mysql에 이해시키려고 함.
        #파이썬 코드를 마이스큐엘에 알아듣게 보내는데 성공함, 버튼 클릭 시 이제 db에 3씩 값이 추가됨 
        cmd += "UPDATE`PALME` SET `commits` = `commits`+ %s WHERE `name` = 'ang'" % KEYWORD['ang']
        self.runCommand(cmd)

    def __del__(self):
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()


##===============================================
##===============================================

# 그저 실행확인기
# if __name__ == '__main__':
#     db = 'IU_KISS'
#     tableName = 'PALME'
#
#     dbu = DatabaseUtility(db, tableName)