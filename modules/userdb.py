# This file is part of YourProjectName.
#
# HackSim is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.
#
# HackSim is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

import pdb; 


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

    def get_user_by_info(self, info_key, info_value):

        
        
        for username, user in self.users.items():
            #print(user.info.get(info_key))
            if user.info.get(info_key) == info_value:
                #pdb.set_trace()
                return user  # Return the user object
        return None
    def __str__(self):
        user_db_str = "User Database:\n"
        for username, user in self.users.items():
            user_db_str += f"Username: {username}\n"
            user_db_str += f"Info: {user.info}\n"
        return user_db_str