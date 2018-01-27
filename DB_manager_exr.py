import mysql.connector




#커서를 훼치해서 받아왔다
class CNXOR():
    def mane(self, nameOfpercent):
        f = open('password.py', 'r')
        p = f.read()
        f.close()

        self.cnx =mysql.connector.connect(user='root', database='IU_KISS', password=p, host='127.0.0.1')
        self.cursor = self.cnx.cursor()
        query = ("SELECT COMMITS FROM PALME WHERE akey= '%s'" % nameOfpercent)
        self.cursor.execute(query)
        self.data = self.cursor.fetchone()
        return self.data


    # def __init__하고 def mane(self):를 토쓰해서 하면 백방 에러남 시발것 몰랐다 맥락이 글러먹어서 그런듯



    # def cx(self):
    #     self.cursor.close()
    #     self.cnx.close()

#
cnxor = CNXOR()
# print(cnxor.mane())