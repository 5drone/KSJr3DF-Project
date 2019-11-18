import pymysql


class DBController:
    def __init__(self):
        self.conn = pymysql.connect(host="207.148.109.78",
                                    user="root",
                                    password="dhgheowkdrns",
                                    db="5ho_general")
        self.curs = self.conn.cursor()


    # SQL SELECT문(LOGIN 테이블)
    def selectSQL_login(self, values):
        sql = "SELECT USER_ID, USER_PW, E_MAIL FROM LOGIN WHERE USER_ID = '%s'"%values[0]
        if self.curs.execute(sql):
            result = self.curs.fetchall()
            return result
        else:
            return False


    # SQL INSERT문(LOGIN 테이블)
    def insertSQL_login(self, values):
        sql ="INSERT INTO LOGIN (USER_ID, USER_PW, E_MAIL) VALUES('%s','%s','%s');"%(values[0], values[1], values[2])
        flag = self.curs.execute(sql)
        self.conn.commit()
        return flag


if __name__=="__main__":
    test = DBController()
    test.selectSQL_login(["gd","gd"])
    """
    def updateSQL(self):
        sql = "UPDATE LOGIN SET USER_ID = "cmc" WHERE USER_ID = "1ho";"
    """

    #def deleteSQL(self):

