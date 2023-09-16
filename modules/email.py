import random
import string

class Email:
    def __init__(self, sender, recipient, subject, message):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.message = message

class EmailClient:
    def __init__(self, username):
        self.inbox = []
        self.username = username
        self.address = self.generate_random_email(self.username)


    def generate_random_email(self, username):
        # List of common email domains
        domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "aol.com", "icloud.com"]

        # Modify the username slightly (e.g., add random characters)
        modified_username = username + "".join(random.choices("0123456789", k=3))

        # Randomly select an email domain
        domain = random.choice(domains)

        # Create the email address
        email = f"{modified_username}@{domain}"

        return email
#     def generate_random_email(self):
#         sender = random.choice(self.users)
#         recipient = random.choice(self.users)
#         subject = ''.join(random.choice(string.ascii_letters) for _ in range(10))
#         message = ''.join(random.choice(string.ascii_letters + ' ') for _ in range(50))
#         return Email(sender.email, recipient.email, subject, message)

#     def send_random_emails(self, num_emails):
#         for _ in range(num_emails):
#             email = self.generate_random_email()
#             self.inbox.append(email)

#     def check_inbox(self):
#         if not self.inbox:
#             print("Inbox is empty.")
#         else:
#             print("Inbox:")
#             for index, email in enumerate(self.inbox, start=1):
#                 print(f"{index}. From: {email.sender}, Subject: {email.subject}")

#     def read_email(self, index):
#         if 1 <= index <= len(self.inbox):
#             email = self.inbox[index - 1]
#             print(f"From: {email.sender}")
#             print(f"To: {email.recipient}")
#             print(f"Subject: {email.subject}")
#             print(f"Message: {email.message}")
#         else:
#             print("Invalid email index.")

# # Create a list of random users
# users = [User('user1', 'example.com'), User('user2', 'example.com'), User('user3', 'example.com')]

# # Example usage:
# email_client = EmailClient(users)
# email_client.send_random_emails(5)
# email_client.check_inbox()
# email_client.read_email(1)
