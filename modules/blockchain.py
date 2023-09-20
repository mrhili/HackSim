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
class Blockchain:
    def __init__(self):
        self.wallets = {}  # Store email clients by username

    def add_wallet(self, username, wallet):
        self.cliwalletsents[username] = wallet

    def get_wallet(self, username):
        return self.wallets.get(username)