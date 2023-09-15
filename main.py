import os
import platform
from modules.bitcoin import BitcoinWallet
# Define simulated files and folders
simulated_files = [
    "file1.txt",
    "file2.py",
    "file3.doc",
    "file4.jpg",
]

# Simulate the default Kali Linux folders
simulated_folders = [
    "Desktop",
    "Downloads",
    "Documents",
    "Pictures",
    "Music",
]

# Define colors for file types
color_mapping = {
    "file": "\033[0;37m",  # White text for files
    "folder": "\033[0;34m",  # Blue text for folders
}

def simulate_ls():
    # Simulate the 'ls' command
    for item in simulated_folders + simulated_files:
        item_type = "folder" if item in simulated_folders else "file"
        color = color_mapping[item_type]
        print(f"{color}{item}\033[0m")  # Reset color to default
def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')  # On Windows, use 'cls' to clear the screen
    else:
        os.system('clear')  # On Unix-like systems, use 'clear'

def main():
    wallet = BitcoinWallet(initial_balance=1000)
    print("Welcome to the Kali Linux Simulation!")
    while True:
        print("$ ", end="")  # Simulate a shell prompt
        user_input = input()

        if user_input == "ls":
            simulate_ls()
        elif user_input == "help":
            print("Available commands:")
            print("ls - List files and folders")
            print("help - Show available commands")
            print("man <command> - Show detailed information about command")
            print("halt - Quit the shell simulation")
            print("bitcoin - Interact with Bitcoin Blockchain")
            print("clear - Clear the screen")
        elif user_input == "clear":
            clear_screen()
        elif user_input.startswith("man "):
            command = user_input.split(" ")[1]
            if command == "ls":
                print("LS Command\n"
                      "============\n"
                      "The 'ls' command is used to list files and folders in the current directory.\n\n"
                      "Usage:\n"
                      "  ls\n\n"
                      "Options:\n"
                      "  None\n")
            elif command == "help":
                print("HELP Command\n"
                      "============\n"
                      "The 'help' command displays available commands and their descriptions.\n\n"
                      "Usage:\n"
                      "  help\n")
            elif command == "halt":
                print("HALT Command\n"
                      "============\n"
                      "The 'halt' command quits the shell simulation.\n\n"
                      "Usage:\n"
                      "  halt\n")
            elif command == "clear":
                print("Clear Command\n"
                      "============\n"
                      "The 'clear' command clear the screen.\n\n"
                      "Usage:\n"
                      "  clear\n")
            elif command == "bitcoin":
                print("Bitcoin Command\n"
                      "============\n"
                      "The 'bitcoin' command to interact with bitcoin blockchain.\n\n"
                      "Usage:\n"
                      "  bitcoin -a ( To print youre address)\n"
                      "  bitcoin -b ( To check youre balance)\n"
                      "  bitcoin -s <Wallet address> -m <amount> ( To send money to an address )\n"
                      "  bitcoin\n")
            else:
                print(f"Command not found: {command}")
        elif user_input.startswith("bitcoin"):
            bitcoin_args = user_input.split(" ")
            if len(bitcoin_args) == 1:
                print("Invalid bitcoin command. Usage: bitcoin -a | -b | -s <address> -m <amount>")
            elif bitcoin_args[1] == "-a":
                print(f"Your Bitcoin Address: {wallet.get_address()}")
            elif bitcoin_args[1] == "-b":
                print(f"Your Bitcoin Balance: {wallet.get_balance()} BTC")
            elif bitcoin_args[1] == "-s" and len(bitcoin_args) >= 6:
                recipient_address = bitcoin_args[3]
                amount = float(bitcoin_args[5])
                result = wallet.send_bitcoins(recipient_address, amount)
                print(result)
            else:
                print("Invalid bitcoin command. Usage: bitcoin -a | -b | -s <address> -m <amount>")
        elif user_input == "halt":
            print("Exiting the Kali Linux Simulation. Goodbye!")
            return  # Exiting the script with 'return' instead of 'break'
        else:
            print(f"Command not found: {user_input}")

if __name__ == "__main__":
    main()