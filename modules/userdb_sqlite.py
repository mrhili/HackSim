import sqlite3
import uuid
import hashlib
import logging
import json

logging.basicConfig(filename="errors.log", filemode="w", level=logging.DEBUG)

class CustomUser():
    def __init__(self, login, password, infos={}) -> None:
        self.login = login
        self.password = password
        self.infos = infos

    def add_info(self, key, value):
        self.infos[key] = value
    
    def get_info(self, key):
        return self.infos.get(key)
    
    def __str__(self) -> str:
        return f"Username: {self.username}\nInfos: {self.infos}"
    
class DB():
    def __init__(self):
        conn = sqlite3.connect("HacksimDb.db")
        self.conn = conn
        conn.execute('''CREATE TABLE IF NOT EXISTS USER
                                            (LOGIN TEXT NOT NULL,
                                            PASSWORD TEXT NOT NULL,
                                            INFOS TEXT NOT NULL);
                     ''')
        conn.commit()

    def hashPassword(self, password):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ":" + salt

    def selectByLogin(self, login):
        try:
            cursor = self.conn.execute("SELECT LOGIN, PASSWORD FROM USER WHERE LOGIN = '%s'" % login)
            user = cursor.fetchone()
            if user == None:
                return False
            return user
        except Exception as ex:
            logging.error("selectionByLogin failed,got this message : %s" % ex)

    def register(self, user):
        try:
            if self.selectByLogin(user.login) == False:
                self.conn.execute("INSERT INTO USER (LOGIN, PASSWORD, INFOS)\
                                VALUES ('%s', '%s', '%s')" % (user.login, self.hashPassword(user.password), json.dumps(user.infos)))
                self.conn.commit()
                return True
            else:
                return False
        except Exception as ex:
            logging.error("registration failed,got this message : %s" % ex)

    def login(self, login, password):
        user = self.selectByLogin(login)
        if user == False:
            return False
        hpassword, salt = user[1].split(":")
        return hpassword == hashlib.sha256(salt.encode() + password.encode()).hexdigest()
