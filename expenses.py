
import json
import os
from datetime import datetime

DATA_FILE = "data/expenses.json"
os.makedirs("data", exist_ok=True)

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(text):
    today = datetime.now().strftime("%Y-%m-%d")

    # Naive amount extraction
    words = text.split()
    amount = None
    for word in words:
        if word.replace('.', '', 1).isdigit():
            amount = float(word)
            break

    if amount is None:
        return "Couldn't find an amount in your message."

    expense = {
        "text": text,
        "amount": amount,
        "date": today
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    return f"Noted! Logged ₹{amount} for: “{text}” on {today}."

def list_today_expenses():
    today = datetime.now().strftime("%Y-%m-%d")
    expenses = [e for e in load_expenses() if e["date"] == today]
    if not expenses:
        return "No expenses for today."

    total = sum(e["amount"] for e in expenses)
    details = "\n".join([f"- ₹{e['amount']}: {e['text']}" for e in expenses])
    return f"Today's expenses:\n{details}\nTotal: ₹{total}"

def list_all_expenses():
    expenses = load_expenses()
    if not expenses:
        return "No expense data found."

    total = sum(e["amount"] for e in expenses)
    details = "\n".join([f"{e['date']}: ₹{e['amount']} - {e['text']}" for e in expenses])
    return f"All Expenses:\n{details}\nTotal Spent: ₹{total}"
