import random
import string

class BitcoinWallet:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.address = self.generate_simulated_bitcoin_address()

    def get_balance(self):
        return self.balance

    def get_address(self):
        return "Your Bitcoin Address "+self.address

    def send_bitcoins(self, recipient_address, amount):
        if amount <= 0:
            return "Invalid amount."

        if self.balance >= amount:
            self.balance -= amount
            return f"Sent {amount} BTC to {recipient_address} (simulated)"
        else:
            return "Insufficient balance (simulated)"

    
    def generate_simulated_bitcoin_address(self):
        # Define the length of the simulated address (typically 26-35 characters)
        address_length = random.randint(26, 35)
        
        # Generate a random address using uppercase letters and digits
        characters = string.ascii_uppercase + string.digits
        simulated_address = ''.join(random.choice(characters) for _ in range(address_length))
        
        return simulated_address