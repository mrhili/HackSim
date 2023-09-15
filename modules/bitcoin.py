import random
import string
import pickle  # Import the pickle module
import os
WALLET_STATE_FILENAME = "wallet_state.pkl"
class BitcoinWallet:
    def __init__(self, initial_balance=0):
        self.initial_balance = initial_balance
        self.load_wallet_state()


    def load_wallet_state(self):
        # Load and deserialize the wallet state from a file
        if os.path.exists(WALLET_STATE_FILENAME):
            with open(WALLET_STATE_FILENAME, "rb") as file:
                wallet = pickle.load(file)
                self.balance = wallet["balance"]
                self.address = wallet["address"]

        else:
            self.balance = self.initial_balance
            self.address = self.generate_simulated_bitcoin_address()
            self.save_functionality()

    def save_functionality(self):
        self.save_wallet_state(self.balance, self.address)
    def rip_functionality(self):
        self.rip_wallet_state()
        self.load_wallet_state()
        self.save_functionality()

    def save_wallet_state(self, b, a):
        # Serialize and save the wallet state to a file
        with open(WALLET_STATE_FILENAME, "wb") as file:
            pickle.dump({"balance":b,"address": a}, file)
    def rip_wallet_state(self):
        if os.path.exists(WALLET_STATE_FILENAME):
            os.remove(WALLET_STATE_FILENAME)

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