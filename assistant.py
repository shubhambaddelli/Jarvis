from tasks import list_all_tasks, list_today_tasks, load_tasks, add_task, save_tasks
from expenses import add_expense, list_today_expenses, list_all_expenses


def handle_input(user_input:str) -> str:
    user_input=user_input.lower()

    if "remind" in user_input or "reminder" in user_input:
        return handle_reminder(user_input)
    elif "expense" in user_input or "spent" in user_input or "track" in user_input:
        return handle_expense(user_input)
    elif "routine" in user_input or "plan my day" in user_input:
        return handle_routine(user_input)
    elif "diet" in user_input or "meal" in user_input:
        return handle_diet(user_input)
    elif "summary" in user_input or "report" in user_input:
        return handle_summary(user_input)
    elif "hi" in user_input or "hello" in user_input or "hey" in user_input:
        return handle_greet(user_input)
    else:
        return "I'm not sure how to help with that yet."


def handle_reminder(text):
    lowered = text.lower()
    if any(word in lowered for word in ["show", "list", "view", "display"]):
        if "today" in text:
            return list_today_tasks()
        elif "all" in text:
            return list_all_tasks()
    else:
        return add_task(text)

def handle_expense(text):
    lowered = text.lower()

    if any(word in lowered for word in ["show", "list", "view", "display"]):
        if "today" in lowered:
            return list_today_expenses()
        elif "all" in lowered:
            return list_all_expenses()
    else:
        return add_expense(text)
def handle_routine(text): return "Routine planner coming soon!"
def handle_diet(text): return "Diet assistant coming soon!"
def handle_summary(text): return "Summary and reports coming soon!"
def handle_greet(text): return "Hello, How can help you today?"

