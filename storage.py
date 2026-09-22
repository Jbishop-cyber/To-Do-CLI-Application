import json


def save_json(tasks):
    with open("Task.json", "w") as file:
        json.dump(tasks, file, indent=2)


def load_json():
    try:
        with open("Task.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nJson file not found or Corrupted")
        return []
