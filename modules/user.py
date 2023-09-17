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

class User:
    def __init__(self, username, info):
        self.username = username
        self.info = info

    def add_info(self, key, value):
        self.info[key] = value

    def get_info(self, key):
        return self.info.get(key)