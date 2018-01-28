#!/usr/bin/python

import mysql.connector
from mysql.connector import errorcode
from datetime import datetime



KEYWORD = dict()
KEYWORD = {'bng':4}
KEYWORD['typeNameOfSubject'] = int(1)
print(KEYWORD)
DICTA = {'subjectName':'iudiary', 'TD LABEL': 'pr44'}



#얘가 직접 일하는 애지, 보내는 애이기도 하고
class DatabaseUtility:



    def __init__(self, database, tableName):
        f = open('password.py', 'r')
        p = f.read()
        f.close()
        self.db = database

        self.tableName = tableName
        self.cnx = mysql.connector.connect(user='root', password=p, host='127.0.0.1')
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


        #이건 테이블이 없을 경우에만 동작하는 것이므로 지금이미 만든 상태에선 그닥 에러를 끼치지 않고 있는 것
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

    def addEntryToTable(self, text):
        #시간을 단순하게 하나의 코드로 짰다 저 안에 들어가는 포맷을 넣고빼고하면서 조작 가능
        datims = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #sftpy에서 보낸 커밋메시지를 커밋메시지 함에 기록한다
        # (이거 변경하느라 시간이.. 아무튼 하나의 칼럼을 추가제거하면 실행할때 필요조건(반드시 엮이는 것이 빠지는지)인 것이 사라지는지 확인 필요)
        cmd = " INSERT INTO " + self.tableName + " (`datim`, `message`)"
        cmd += " VALUES ('%s', '%s');" % (datims, text)
        "where"

        #딕트쌍으로 과목-인상시킬 포인트를 짜고, 스트링테크닉으로 mysql에 이해시키려고 함.
        #파이썬 코드를 마이스큐엘에 알아듣게 보내는데 성공함, 버튼 클릭 시 이제 db에 3씩 값이 추가됨
        cmd += "UPDATE`PALME` SET `commits` = `commits`+ %s WHERE `name` = '%s'" % (KEYWORD['typeNameOfSubject'], DICTA['subjectName'])
        self.runCommand(cmd)







    #쓰이지 않을 것 같다
    # def toMysqlwithKey(self):
    #     cmd = "SELECT COMMITS FROM `PALME` WHERE `id`=1"
    #     # print(akey)
    #     self.runCommand(cmd)





#이 종료자가 꼭 필요한가?
    # def __del__(self):
    #     self.cnx.commit()
    #     self.cursor.close()
    #     self.cnx.close()


##===============================================
##===============================================

# 그저 실행확인기
# if __name__ == '__main__':
#     db = 'IU_KISS'
#     tableName = 'PALME'
#
#     dbu = DatabaseUtility(db, tableName)