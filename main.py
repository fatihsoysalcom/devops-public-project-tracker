import json
import os
from datetime import datetime

# This script simulates a simple public project tracker for a DevOps engineer.
# It allows logging progress, challenges, and learnings, making them publicly visible.

PROJECT_FILE = "public_project_log.json"

def load_log():
    """Loads the project log from a JSON file."""
    if os.path.exists(PROJECT_FILE):
        with open(PROJECT_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_log(log):
    """Saves the project log to a JSON file."""
    with open(PROJECT_FILE, 'w', encoding='utf-8') as f:
        json.dump(log, f, indent=4, ensure_ascii=False)

def add_entry(log, entry_type, message):
    """Adds a new entry to the log."""
    timestamp = datetime.now().isoformat()
    log.append({
        "timestamp": timestamp,
        "type": entry_type,  # e.g., 'progress', 'challenge', 'learning'
        "message": message
    })
    print(f"Added '{entry_type}' entry: {message}")

def view_log(log):
    """Prints the current project log."""
    if not log:
        print("Project log is empty.")
        return
    print("\n--- Public Project Log ---")
    for entry in log:
        print(f"[{entry['timestamp']}] ({entry['type'].capitalize()}): {entry['message']}")
    print("------------------------\n")

def main():
    project_log = load_log()

    print("Welcome to your Public DevOps Project Tracker!")
    print("This tool helps you log your progress, challenges, and learnings publicly.")

    while True:
        print("Options: add [progress|challenge|learning] <message>, view, exit")
        command = input("> ").strip().lower()

        if command.startswith("add "):
            parts = command.split(maxsplit=2)
            if len(parts) == 3:
                entry_type = parts[1]
                message = parts[2]
                if entry_type in ["progress", "challenge", "learning"]:
                    add_entry(project_log, entry_type, message)
                    save_log(project_log)
                else:
                    print("Invalid entry type. Use 'progress', 'challenge', or 'learning'.")
            else:
                print("Usage: add [progress|challenge|learning] <message>")
        elif command == "view":
            view_log(project_log)
        elif command == "exit":
            print("Exiting tracker. Your log is saved.")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
