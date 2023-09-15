import os

# Define simulated files and folders
simulated_files = [
    "file1.txt",
    "file2.py",
    "file3.doc",
    "file4.jpg",
]

simulated_folders = [
    "docs",
    "pictures",
    "downloads",
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

def main():
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
        elif user_input == "man ls":
            print("LS Command\n"
                  "============\n"
                  "The 'ls' command is used to list files and folders in the current directory.\n\n"
                  "Usage:\n"
                  "  ls\n\n"
                  "Options:\n"
                  "  None\n")
        else:
            print(f"Command not found: {user_input}")

if __name__ == "__main__":
    main()
