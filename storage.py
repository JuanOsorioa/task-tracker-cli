import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []   # Return an empty list if the file do not exist
    
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file_json: # Load configuration
            return json.load(file_json)
    except json.JSONDecodeError:
        print("ATENTION: The JSON file is corrupted or empty, \nStartin a clean list")
        return []

def save_tasks(tasks_list):
    with open(FILE_NAME, "w", encoding="UTF-8") as file_json: # Write configuration
        return json.dump(tasks_list, file_json, indent=4)

