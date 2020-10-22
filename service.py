from .utils import encrypt
from .models import insert_into_db, get_agent_credential, get_items_from_db, save_todo_item_in_db


def register_agent(agent_id, password):
    encripted_pass = encrypt(password)
    insert_into_db(agent_id, encripted_pass)


def authenticate_agent(agent_id, password):
    encripted_pass = encrypt(password)
    agent = get_agent_credential(agent_id)
    stored_password = agent.get("password")
    if stored_password == encripted_pass:
        return True, agent.get("agent_id")
    return False, None


def get_todo_items(agent_id):
    todo_items = []
    items = get_items_from_db(agent_id)
    for item in items:
        todo_items.append({
            "title": item.get("title"),
            "description": item.get("description"),
            "category": item.get("category"),
            "due_date": item.get("due_date")
        })
    return todo_items


def save_todo_item(agent_id, title, description, category, due_date):
    save_todo_item_in_db(agent_id, title, description, category, due_date)
