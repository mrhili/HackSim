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

import random
import string
from .rand import generate_random_email_address
from tabulate import tabulate

class Email:
    def __init__(self, sender, recipient, subject, message, reference=None):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.message = message
        self.reference = None
        if reference:
            self.s=reference = reference

class EmailClient:
    def __init__(self, username):
        self.inbox = []
        self.outbox = []
        self.username = username
        self.address = generate_random_email_address(self.username)

    def send_email(self, receiver, subject="", message=""):

        email = Email(self.username, receiver.username, subject, message)

        receiver.receive_email(self, email)

    def receive_email(self, sender, email):

        self.inbox.append({"sender":email.sender,"subject":email.subject,"message":email.message})

    # def respond_to_email(self, email, message):
    #     reply = {
    #         "from": self.username,
    #         "to": email["from"],
    #         "subject": f"Re: {email['subject']}",
    #         "message": message,
    #     }
    #     recipient_email_client = self.userdb.get_user(email["from"]).get_info("email_client")
    #     if recipient_email_client:
    #         recipient_email_client.receive_email(reply)
    #     else:
    #         self.userdb.get_user(email["from"]).inbox.append(reply)

    
    def check_inbox(self):
        if not self.inbox:
            print("Inbox is empty.")
            return

        inbox_data = []

        
        for i, email in enumerate(self.inbox[::-1]):
            # print(f"Email {i+1}:")
            # print(f"From: {email['sender']}")
            # #print(f"To: {email['recipient']}")
            # print(f"Subject: {email['subject']}")
            # print(f"Message: {email['message']}")
            # print("-" * 40)

            inbox_data.append([
                f"Email {len(self.inbox) - self.inbox.index(email)}",
                email["sender"],
                email["subject"],
                email["message"]
            ])

            print("Inbox:")
        table = tabulate(inbox_data, headers=["Email #", "From", "Subject", "Message"], tablefmt="pretty")
        print(table)









