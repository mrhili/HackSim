import os
import platform
import pickle  # Import the pickle module
from modules.bitcoin import BitcoinWallet
from modules.email import Email, EmailClient
from modules.user import User
from modules.userdb import UserDB
import json
from prompt_toolkit import prompt

folder_structure = {
    "freelance": {
        "easy_blabla_10.txt": {
            "spec": {
                "inside": "Crack the password for user123.",
                "reward": 10,
                "type":"file"
            }
        },
        "folda": {
            "spec": {
                "type":"folder"
            }
        },
        "spec":{
            "type":"folder"
        }
    }
}

current_dir = list(folder_structure.keys())[0]

# Define colors for file types
color_mapping = {
    "file": "\033[0;37m",  # White text for files
    "folder": "\033[0;34m",  # Blue text for folders
}

def format_prompt(username, computername, path):
    return f"┌──({username}㉿{computername})-[{path}]\n└─$ "


def reset_game():
    # Delete the wallet state file to reset the game
    if os.path.exists(WALLET_STATE_FILENAME):
        os.remove(WALLET_STATE_FILENAME)
    print("Game reset. Initial balance set to 1000 BTC.")




def simulate_cd(args):
    global current_dir

    if args:
        new_dir = args[0]

        if new_dir == "..":
            # Move up one level
            current_path_parts = current_dir.split("/")
            if len(current_path_parts) > 1:
                current_dir = "/".join(current_path_parts[:-1])
            else:
                current_dir = ""
        else:
            current_dir_contents = folder_structure.get(current_dir, {})
            if new_dir in current_dir_contents and current_dir_contents[new_dir]["spec"]["type"] == "folder":
                new_path = os.path.join(current_dir, new_dir).replace("\\", "/")
                current_dir = new_path
            else:
                print(f"cd: {new_dir}: No such folder")




# Usage example:
# simulate_ls([])  # List contents of the current directory
# simulate_ls(["folda"])  # List contents of the 'folda' directory



def simulate_ls(args):
    current_location = folder_structure

    if args and args[0] == "/":
        current_location = folder_structure  # List the root directory
    else:
        # Navigate to the specified directory
        for dir_name in current_dir.split("/"):
            if dir_name:
                current_location = current_location[dir_name]

        # Check if there are additional arguments (e.g., "/freelance/folda")
        if args:
            for arg in args:
                if arg in current_location and arg != "spec":
                    current_location = current_location[arg]
                else:
                    print(f"ls: cannot access '{'/'.join(args)}': No such file or directory")
                    return

    for item, properties in current_location.items():
        if item != "spec":
            item_type = properties.get("spec", {}).get("type", "file")
            color = color_mapping[item_type]
            print(f"{color}{item}\033[0m")

def man_ls():
    print("LS Command\n"
        "============\n"
        "The 'ls' command is used to list files and folders in the current directory.\n\n"
        "Usage:\n"
        "  ls\n\n"
        "Options:\n"
        "  None\n")

def man_mutt():
    print("Usage: mutt [OPTIONS]")
    print("Options:")
    print("  -a   Show your email address")
    print("  -h   Display help message")


def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')  # On Windows, use 'cls' to clear the screen
    else:
        os.system('clear')  # On Unix-like systems, use 'clear'

def main():

    username = input("Choose youre username : ")
    player = User(username, info={})

    computername = input("Choose youre Computer Name : ")

    init_balance = 1000
    wallet = BitcoinWallet(initial_balance=init_balance)

    player.add_info("bitcoin_address", wallet.get_address())

    userdb = UserDB()
    userdb.add_user(player)

    myMails = EmailClient(username = username)

    userdb.update_user(username, "email",myMails.address)

    print("Welcome to the Kali Linux Simulation!")
    while True:
        user_input = prompt(format_prompt(username,computername,current_dir))
        command_args = user_input.split()

        if not command_args:
            continue

        command = command_args[0]
        args = command_args[1:]

        if command == "ls":
            simulate_ls(args)
        elif command == "cd":
            simulate_cd(args)
        elif user_input == "help":
            print("Available commands:")
            print("ls - List files and folders")
            print("help - Show available commands")
            print("man <command> - Show detailed information about command")
            print("halt - Quit the shell simulation")
            print("bitcoin - Interact with Bitcoin Blockchain")
            print("mutt - Mail Interface")
            print("whoami - Fetch username")
            print("clear - Clear the screen")
        elif user_input == "clear":
            clear_screen()
        
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
            wallet.save_functionality()
            print("Exiting the Kali Linux Simulation. Goodbye!")
            return  # Exiting the script with 'return' instead of 'break'
        elif user_input == "reset":
            wallet.rip_functionality()
            print("Reseting Wallet state")
        elif user_input == "whoami":
            print(username)
        elif user_input.startswith('mutt'):
            # Split the user input into command and options
            parts = user_input.split()
            if len(parts) == 1:
                man_mutt()
            elif len(parts) == 2:
                option = parts[1]
                if option == '-a':
                    # Simulate checking the email address
                    print(f"Your email address is: {myMails.address}")
                elif option == '-h':
                    # Display help
                    man_mutt()
                else:
                    print("Unrecognized option. Use 'mutt -h' for help.")
            else:
                print("Invalid command. Use 'mutt -h' for help.")
        elif user_input.startswith("man "):
            command = user_input.split(" ")[1]
            if command == "ls":
                man_ls()
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
            elif command == "reset":
                print("Clear Command\n"
                      "============\n"
                      "The 'reset' command Reset the game progress.\n\n"
                      "Usage:\n"
                      "  reset\n")
            elif command == "mutt":
                man_mutt()
            elif command == "whoami":
                print("Fetch username")
            else:
                print(f"No manual for : {command}")
        else:
            print(f"Command not found: {user_input}")

if __name__ == "__main__":
    main()
