import json
import os
from datetime import datetime

DATA_FILE="data/tasks.json"

os.makedirs("data", exist_ok=True)

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(text):
    # Simple date extraction (can improve later)
    today = datetime.now().strftime("%Y-%m-%d")
    task = {
        "text": text,
        "date": today  # For now, we'll assign everything to today
    }

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

    return f"Got it! I’ve added the reminder: “{text}” for {today}."

def list_today_tasks():
    today = datetime.now().strftime("%Y-%m-%d")
    tasks = load_tasks()
    today_tasks = [task["text"] for task in tasks if task["date"] == today]

    if not today_tasks:
        return "You have no reminders for today."
    return "Today's reminders:\n- " + "\n- ".join(today_tasks)

def list_all_tasks():
    tasks = load_tasks()
    if not tasks:
        return "No reminders saved yet."
    return "All reminders:\n" + "\n".join(
        [f"{task['date']}: {task['text']}" for task in tasks]
    )