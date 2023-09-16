class UserDB:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def get_user(self, username):
        return self.users.get(username)

    def update_user(self, username, key, value):
        user = self.get_user(username)
        if user:
            user.add_info(key, value)
        else:
            print(f"User '{username}' not found in the database.")
