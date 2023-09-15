import os
import platform
import json
from modules.bitcoin import BitcoinWallet

# Define a dictionary to represent the folder and file structure
folder_structure = {
    "freelance": {
        "easy_blabla_10.txt": {
            "spec": {
                "inside": "Crack the password for user123.",
                "reward": 10,
                "type":"file"
            }
        },
        "spec":{
            "type":"folder"
        }
    }
}

# ... (rest of your code) ...

current_directory = list(folder_structure.keys())[0] # Initial directory

def navigate_directory(new_directory):
    global current_directory
    # Check if the new directory exists within the current directory
    if new_directory in folder_structure.get(current_directory, {}):
        current_directory = new_directory
    else:
        print(f"Directory '{new_directory}' not found.")

def list_jobs():
    jobs = folder_structure.get(current_directory, {})
    for job_name, job_details in jobs.items():
        print(f"{job_name} - Difficulty: {current_directory.capitalize()}, Reward: {job_details['reward']} BTC")

def view_job(job_name):
    jobs = folder_structure.get(current_directory, {})
    job_details = jobs.get(job_name)
    if job_details:
        print(f"Job: {job_name}")
        print(f"Difficulty: {current_directory.capitalize()}")
        print(f"Reward: {job_details['reward']} BTC")
        print(f"Description: {job_details['description']}")
    else:
        print(f"Job '{job_name}' not found.")

# Main loop
while True:
    user_input = input(f"{current_directory}$ ")
    if user_input.startswith("cd "):
        new_directory = user_input.split(" ", 1)[1]
        navigate_directory(new_directory)
    elif user_input == "ls":
        list_jobs()
    elif user_input.startswith("cat "):
        job_name = user_input.split(" ", 1)[1]
        view_job(job_name)
    elif user_input == "exit":
        print("Exiting the simulation. Goodbye!")
        break
    else:
        print(f"Command not found: {user_input}")
