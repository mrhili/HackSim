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

class EmailClientManager:
    def __init__(self):
        self.clients = {}  # Store email clients by username

    def add_client(self, username, email_client):
        self.clients[username] = email_client

    def get_client(self, username):
        return self.clients.get(username)

    # def send_email(self, sender, receiver_address, subject="", message=""):
    #     sender_client = self.get_client(sender.username)
    #     if sender_client:
    #         receiver_client = self.get_client(receiver_address.split('@')[0])  # Assuming username is before '@'
    #         if receiver_client:
    #             email = Email(sender.address, receiver_address, subject, message)
    #             sender_client.send_email(receiver_client, email)
    #         else:
    #             print("Error: Receiver's email client not found.")
    #     else:
    #         print("Error: Sender's email client not found.")

    # Implement other methods as needed to manage email clients globally