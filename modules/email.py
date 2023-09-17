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
        self.reference = reference

    def __str__(self):
        email_str = f"From: {self.sender}\n"
        email_str += f"To: {self.recipient}\n"
        email_str += f"Subject: {self.subject}\n"
        email_str += f"Message:\n{self.message}\n"

        if self.reference:
            email_str += f"Reference: {self.reference}\n"

        return email_str

class EmailClient:
    def __init__(self, username):
        self.inbox = []
        self.outbox = []
        self.username = username
        self.address = generate_random_email_address(self.username)

    def send_email(self, receiver, subject="", message=""):

        email = Email(self.address, receiver.address, subject, message)

        self.inbox.append({"recipient":email.recipient,"subject":email.subject,"message":email.message, "reference": None})

        receiver.receive_email(self, email)

    def receive_email(self, sender, email):

        self.inbox.append({"sender":sender.address,"subject":email.subject,"message":email.message, "reference": None})

    def respond_to_email(self, index, subject="", message=""):

        ref_email = self.inbox[index]

        if ref_email:

            receiver_address = ref_email["sender"]

            reference = ref_email

            email = Email(self.address, receiver.address, subject, message, reference)

            self.inbox.append({"recipient":email.recipient,"subject":email.subject,"message":email.message, "reference": reference})

            receiver.receive_email(self, email)
        else:
            print("Error in refencing email to respond on")
        
    
    def check_inbox(self):
        if not self.inbox:
            print("Inbox is empty.")
            return

        inbox_data = []

        
        for i, email in enumerate(self.inbox[::-1]):

            inbox_data.append([
                f"Email {len(self.inbox) - self.inbox.index(email)}",
                email["sender"],
                email["subject"],
                email["message"],
                str(email) if email["reference"] else "No reference"
            ])

            print("Inbox:")
        table = tabulate(inbox_data, headers=["Email #", "From", "Subject", "Message", "Reference Email"], tablefmt="pretty")
        print(table)









