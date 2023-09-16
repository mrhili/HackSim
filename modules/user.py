class User:
    def __init__(self, username, info):
        self.username = username
        self.info = info

    def add_info(self, key, value):
        self.info[key] = value

    def get_info(self, key):
        return self.info.get(key)