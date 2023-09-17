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

def generate_username(length=8):
    characters = string.ascii_letters + string.digits
    username = ''.join(random.choice(characters) for _ in range(length))
    return username


def generate_random_email_address(username):
    # List of common email domains
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "aol.com", "icloud.com"]

    # Modify the username slightly (e.g., add random characters)
    modified_username = username + "".join(random.choices("0123456789", k=3))

    # Randomly select an email domain
    domain = random.choice(domains)

    # Create the email address
    email = f"{modified_username}@{domain}"

    return email

def generate_simulated_bitcoin_address():
    # Define the length of the simulated address (typically 26-35 characters)
    address_length = random.randint(26, 35)
    
    # Generate a random address using uppercase letters and digits
    characters = string.ascii_uppercase + string.digits
    simulated_address = ''.join(random.choice(characters) for _ in range(address_length))

    return simulated_address