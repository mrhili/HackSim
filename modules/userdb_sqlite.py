import sqlite3
import uuid
import hashlib
import logging
import json

logging.basicConfig(filename="errors.log", filemode="w", level=logging.DEBUG)

class CustomUser():
    def __init__(self, username, password, infos={}):
        self.username = username
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
        conn = sqlite3.connect("hacksim.db")
        self.conn = conn
        conn.execute('''CREATE TABLE IF NOT EXISTS users
                                            (username TEXT NOT NULL,
                                            password TEXT NOT NULL,
                                            infos TEXT NOT NULL);
                     ''')
        conn.commit()

    def hash_password(self, password):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ":" + salt

    def select_by_login(self, username):
        try:
            cursor = self.conn.execute("SELECT username, password FROM users WHERE username = '%s'" % username)
            user = cursor.fetchone()
            if user == None:
                return False
            return user
        except Exception as ex:
            logging.error("selectionByLogin failed, got this message : %s" % ex)

    def register(self, user):
        try:
            if self.select_by_login(user.username) == False:
                self.conn.execute("INSERT INTO users (username, password, infos)\
                                VALUES ('%s', '%s', '%s')" % (user.username, self.hash_password(user.password), json.dumps(user.infos)))
                self.conn.commit()
                return True
            return False
        except Exception as ex:
            logging.error("registration failed, got this message : %s" % ex)

    def login(self, login, password):
        user = self.select_by_login(login)
        if user == False:
            return False
        hpassword, salt = user[1].split(":")
        return hpassword == hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    
    def add_or_update_user_infos(self, username, infos):
        try:
            cursor = self.conn.execute("SELECT infos FROM users WHERE username = '%s'" % username)
            user = cursor.fetchone()
            if user == None:
                return False
            user_infos = json.loads(user[0])
            user_infos.update(infos)
            self.conn.execute("UPDATE users SET infos = '%s' WHERE username = '%s'" % (json.dumps(user_infos), username))
            self.conn.commit()
            return True
        except Exception as ex:
            logging.error("add_or_update_user_infos failed, got this message : %s" % ex)

    def delete_user_infos_by_key(self, username, key):
        try:
            infos = self.get_user_infos(username)
            if infos == False:
                return False
            infos.pop(key)
            self.conn.execute("UPDATE users SET infos = '%s' WHERE username = '%s'" % (json.dumps(infos), username))
            self.conn.commit()
            return True
        except Exception as ex:
            logging.error("delete_user_infos_by_key failed, got this message : %s" % ex)

    def get_user_infos(self, username):
        try:
            cursor = self.conn.execute("SELECT infos FROM users WHERE username = '%s'" % username)
            user = cursor.fetchone()
            if user == None:
                return False
            return json.loads(user[0])
        except Exception as ex:
            logging.error("get_user_infos failed, got this message : %s" % ex)