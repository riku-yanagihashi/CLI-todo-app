import json
import os
from colorama import init, Fore, Style

init(autoreset=True)

DB_FILE = 'todos.json'
CONFIG_FILE = 'config.json'
LANG_DIR = 'languages'
LANG_FILE = 'lang_en.json'

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            return json.load(file)
    return {"language": "en"}

def save_config(config):
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file, indent=4)

def load_language():
    global LANG_FILE
    config = load_config()
    if config['language'] == 'ja':
        LANG_FILE = 'lang_ja.json'
    else:
        LANG_FILE = 'lang_en.json'
    with open(os.path.join(LANG_DIR, LANG_FILE), 'r') as file:
        return json.load(file)

LANG = load_language()

def load_todos():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as file:
            return json.load(file)
    return []

def save_todos(todos):
    with open(DB_FILE, 'w') as file:
        json.dump(todos, file, indent=4)

def display_menu():
    print(Fore.GREEN + "\n" + "="*40)
    print(Fore.GREEN + " " + LANG['menu']['title'])
    print("="*40)
    for option in LANG['menu']['options']:
        print(Fore.YELLOW + option)
    print(Fore.GREEN + "="*40 + "\n")

def add_todo():
    task = input(Fore.CYAN + LANG['messages']['enter_task'])
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print(Fore.GREEN + "\n" + LANG['messages']['todo_added'] + "\n")

def view_todos():
    todos = load_todos()
    if not todos:
        print(Fore.YELLOW + "\n" + LANG['messages']['no_todos'] + "\n")
        return
    print(Fore.GREEN + "\n" + LANG['messages']['your_todos'])
    print(Fore.GREEN + "-"*40)
    for index, todo in enumerate(todos, start=1):
        status = Fore.RED + LANG['status']['not_done'] if not todo["done"] else Fore.GREEN + LANG['status']['done']
        print(Fore.CYAN + f"{index}. {status} {todo['task']}")
    print(Fore.GREEN + "-"*40 + "\n")

def update_todo():
    view_todos()
    todos = load_todos()
    if not todos:
        return
    try:
        index = int(input(Fore.CYAN + LANG['messages']['enter_number_update'])) - 1
        if 0 <= index < len(todos):
            todos[index]["task"] = input(Fore.CYAN + LANG['messages']['enter_new_task'])
            status = input(Fore.CYAN + LANG['messages']['is_done']).strip().lower()
            todos[index]["done"] = status == "yes"
            save_todos(todos)
            print(Fore.GREEN + "\n" + LANG['messages']['todo_updated'] + "\n")
        else:
            print(Fore.RED + "\n" + LANG['messages']['invalid_number'] + "\n")
    except ValueError:
        print(Fore.RED + "\n" + LANG['messages']['invalid_input'] + "\n")

def delete_todo():
    view_todos()
    todos = load_todos()
    if not todos:
        return
    try:
        index = int(input(Fore.CYAN + LANG['messages']['enter_number_delete'])) - 1
        if 0 <= index < len(todos):
            todos.pop(index)
            save_todos(todos)
            print(Fore.GREEN + "\n" + LANG['messages']['todo_deleted'] + "\n")
        else:
            print(Fore.RED + "\n" + LANG['messages']['invalid_number'] + "\n")
    except ValueError:
        print(Fore.RED + "\n" + LANG['messages']['invalid_input'] + "\n")

def main():
    while True:
        display_menu()
        choice = input(Fore.CYAN + LANG['menu']['prompt']).strip().lower()
        if choice in ['1', 'add', 'a']:
            add_todo()
        elif choice in ['2', 'view', 'v']:
            view_todos()
        elif choice in ['3', 'update', 'u']:
            update_todo()
        elif choice in ['4', 'delete', 'd']:
            delete_todo()
        elif choice in ['5', 'exit', 'e']:
            print(Fore.GREEN + "\n" + LANG['messages']['goodbye'] + "\n")
            break
        else:
            print(Fore.RED + "\n" + LANG['messages']['invalid_choice'] + "\n")

if __name__ == "__main__":
    main()
