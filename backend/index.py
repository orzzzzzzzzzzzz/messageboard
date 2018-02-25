from flask import Flask
from flask import request
from flask_cors import *
from sqlconnect import sqlconnect
import hashlib

app = Flask(__name__)
CORS(app, supports_credentials=True)
sqlCon=sqlconnect()

def md5Encode(str):
    m = hashlib.md5()
    m.update(str.encode("utf-8"))
    return m.hexdigest()

@app.route("/register",methods=["POST"])
def register():
    if request.method == 'POST' and request.form.get('username') and request.form.get('password'):
        data = request.form.to_dict()
        username = md5Encode(data.get("username"))
        password = md5Encode(data.get("password"))
        judge=sqlCon.judgeUsername(username)
        if judge == 0:
            result = sqlCon.setRegisterData(username,password)
            if result == 0:
                return "200!"
            else:
                return "emm"
        else:
            return "emmm"
    else:
        return "emmmm"

@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST' and request.form.get('username') and request.form.get('password'):
        data = request.form.to_dict()
        username = md5Encode(data.get("username"))
        password = md5Encode(data.get("password"))
        result = sqlCon.getLoginData(username)
        if not result:
            return "-1"
        elif password != result[0]:
            return "0"
        elif username == "admin" and password == result[0]:
            return "admin"
        else:
            return "1"
    else:
        return "emmm"

@app.route("/store", methods=['POST'])
def store():
    if request.method == 'POST' and request.form.get('username') and request.form.get('message') and request.form.get('newdate'):
        data = request.form.to_dict()
        username = data.get('username')
        message = data.get('message')
        newdate = data.get('newdate')
        result = sqlCon.setMessageData(username,message,newdate)
        if result == 0:
            return "saved"
        else:
            return "emmm"
    else:
        return "emmmm"

@app.route("/getMessage", methods=['GET'])
def getMessage():
    if request.method == 'GET':
        result = sqlCon.getMessageData()
        return result

@app.route("/deleteMessage", methods=['POST'])
def deleteMessage():
    if request.method == 'POST' and request.form.get('username') and request.form.get('message') and request.form.get('newdate'):
        data = request.form.to_dict()
        username = data.get('username')
        message = data.get('message')
        newdate = data.get('newdate')
        result = sqlCon.deleteMessageData(username,message,newdate)
        if result == 0:
            return "deleted"
        else:
            return "emmm"
    else:
        return "emmmm"


if __name__ == '__main__':
    app.run(debug=True)