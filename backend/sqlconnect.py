import pymysql
import json


class sqlconnect:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='userinfo', charset='utf8')
        self.cur = self.conn.cursor()

    def setRegisterData(self,username,password):
        sql = "INSERT INTO info (username, password) VALUES (\'%s\', \'%s\')" % (username, password)
        self.cur.execute(sql)
        self.conn.commit()
        return 0

    def judgeUsername(self,username):
        sql = "SELECT * FROM info WHERE username=\'" + username + "\'"
        self.cur.execute(sql)
        results = self.cur.fetchall()
        if len(results) == 0:
            return 0
        else:
            return ()

    def getLoginData(self,username):
        sql = "SELECT password FROM info WHERE username=\'" + username + "\'"
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if result:
            return result
        else:
            return ()

    def setMessageData(self,username,message,newdate):
        sql = "INSERT INTO notes (username,message,newdate) VALUES (\'%s\',\'%s\',\'%s\')" % (username,message,newdate)
        self.cur.execute(sql)
        self.conn.commit()
        return 0

    def getMessageData(self):
        sql = "SELECT * FROM notes"
        self.cur.execute(sql)
        results = self.cur.fetchall()
        data = []
        for result in results:
            info = {}
            info['username'] = result[0]
            info['message'] = result[1]
            info['newdate'] = result[2]
            data.append(info)
        jsonStr = json.dumps(data)
        return jsonStr

    def deleteMessageData(self,username,message,newdate):
        sql = "DELETE FROM notes WHERE username=\'%s\' AND message=\'%s\' AND newdate=\'%s\'"%(username,message,newdate)
        self.cur.execute(sql)
        self.conn.commit()
        return 0
